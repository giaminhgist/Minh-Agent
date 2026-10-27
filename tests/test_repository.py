import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    value=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


installer=module('installer','tools/install.py')
validator=module('validator','tools/validate.py')
packager=module('packager','tools/package.py')
plot=module('plot','skills/paper-figures/scripts/plot_svg.py')
diagram=module('diagram','skills/technical-diagrams/scripts/render_svg.py')
queue=module('queue','skills/experiment-queue/scripts/local_queue.py')
debt=module('debt','skills/technical-debt-ledger/scripts/scan_debt.py')


class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='minh-skills-test-')
        self.path=Path(self.temp.name)
    def tearDown(self):
        self.temp.cleanup()
    def write(self,name,content):
        path=self.path/name
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(content,encoding='utf-8')
        return path


class InstallerTests(WorkspaceTest):
    def test_dry_run_is_read_only(self):
        dest=self.path/'new'
        result=installer.install(dest,['paper-reading'])
        self.assertEqual(result[0]['action'],'install')
        self.assertFalse(dest.exists())
    def test_install_has_complete_skill_and_receipt(self):
        dest=self.path/'skills'
        installer.install(dest,['paper-figures'],True)
        self.assertEqual(installer.digest_tree(dest/'paper-figures'),installer.digest_tree(ROOT/'skills/paper-figures',ignore_generated=True))
        self.assertFalse(any((dest/'paper-figures').rglob('*.pyc')))
        self.assertTrue((dest/'.minh-agent-receipts/paper-figures.json').is_file())
        # Installed helper must run without the original repository or relative siblings.
        csv=self.write('data.csv','x,y\n1,2\n2,3\n')
        result=subprocess.run([sys.executable,str(dest/'paper-figures/scripts/plot_svg.py'),str(csv),str(self.path/'out.svg'),'--x','x','--y','y'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
    def test_identical_install_is_idempotent(self):
        installer.install(self.path,['paper-reading'],True)
        result=installer.install(self.path,['paper-reading'],True)
        self.assertEqual(result[0]['action'],'unchanged')
    def test_conflict_does_not_overwrite_or_partially_install(self):
        self.write('paper-reading/SKILL.md','user work')
        with self.assertRaises(ValueError):
            installer.install(self.path,['paper-figures','paper-reading'],True)
        self.assertFalse((self.path/'paper-figures').exists())
        self.assertEqual((self.path/'paper-reading/SKILL.md').read_text(),'user work')
    def test_remove_only_unchanged_owned_installation(self):
        installer.install(self.path,['paper-reading'],True)
        installer.install(self.path,['paper-reading'],True,True)
        self.assertFalse((self.path/'paper-reading').exists())
    def test_remove_refuses_modified_skill(self):
        installer.install(self.path,['paper-reading'],True)
        self.write('paper-reading/user-note.txt','keep me')
        with self.assertRaises(ValueError):
            installer.install(self.path,['paper-reading'],True,True)
        self.assertTrue((self.path/'paper-reading/user-note.txt').exists())
    def test_path_traversal_name_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.path,['../outside'],True)
    def test_profile_cli_selects_exact_group(self):
        result=subprocess.run([sys.executable,str(ROOT/'tools/install.py'),'--destination',str(self.path/'skills'),'--profile','Figures & communication'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(len(json.loads(result.stdout)),5)
        self.assertFalse((self.path/'skills').exists())


class PlotTests(WorkspaceTest):
    def test_numeric_svg_and_provenance(self):
        csv=self.write('data.csv','step,score\n1,0.4\n2,0.6\n3,0.7\n')
        out=self.path/'plot.svg'
        metadata=plot.render(csv,out,'step','score',title='A < B & C')
        tree=ET.parse(out)
        self.assertEqual(tree.getroot().find('{http://www.w3.org/2000/svg}title').text,'A < B & C')
        self.assertEqual(len(tree.findall('.//{http://www.w3.org/2000/svg}circle')),3)
        self.assertEqual(metadata['sha256'],hashlib.sha256(csv.read_bytes()).hexdigest())
    def test_nonfinite_rejected_without_artifact(self):
        csv=self.write('data.csv','x,y\n1,nan\n')
        out=self.path/'out.svg'
        with self.assertRaises(ValueError):
            plot.render(csv,out,'x','y')
        self.assertFalse(out.exists())
    def test_missing_column_rejected(self):
        csv=self.write('data.csv','x,z\n1,2\n')
        with self.assertRaises(ValueError):
            plot.render(csv,self.path/'out.svg','x','y')
    def test_line_rejects_silent_reordering(self):
        csv=self.write('data.csv','x,y\n2,2\n1,1\n')
        with self.assertRaises(ValueError):
            plot.render(csv,self.path/'out.svg','x','y')
    def test_negative_bar_geometry(self):
        csv=self.write('data.csv','x,y\n1,-3\n2,5\n')
        out=self.path/'out.svg'
        plot.render(csv,out,'x','y','bar')
        bars=[x for x in ET.parse(out).findall('.//{http://www.w3.org/2000/svg}rect') if x.get('fill')=='#245bba']
        self.assertEqual(len(bars),2)
        self.assertTrue(all(float(x.get('height'))>0 for x in bars))
    def test_refuses_input_overwrite(self):
        csv=self.write('data.csv','x,y\n1,2\n')
        with self.assertRaises(ValueError):
            plot.render(csv,csv,'x','y')
        self.assertEqual(csv.read_text(),'x,y\n1,2\n')


class DiagramTests(unittest.TestCase):
    def setUp(self):
        self.spec={'schema':'simple-diagram-v1','width':600,'height':200,'nodes':[{'id':'a','x':20,'y':60,'width':140,'height':60,'label':'A & B'},{'id':'b','x':400,'y':60,'width':140,'height':60,'label':'Output'}],'edges':[{'source':'a','target':'b'}]}
    def test_editable_svg_and_border_anchors(self):
        root=ET.fromstring(diagram.render(self.spec))
        line=root.find('{http://www.w3.org/2000/svg}line')
        self.assertEqual(float(line.get('x1')),160)
        self.assertEqual(float(line.get('x2')),400)
        texts=[x.text for x in root.findall('.//{http://www.w3.org/2000/svg}text')]
        self.assertIn('A & B',texts)
    def test_missing_endpoint(self):
        self.spec['edges'][0]['target']='missing'
        with self.assertRaises(ValueError):
            diagram.render(self.spec)
    def test_schema_not_silently_converted(self):
        self.spec['schema']='FigureSpec'
        with self.assertRaises(ValueError):
            diagram.render(self.spec)
    def test_overflow_rejected(self):
        self.spec['nodes'][0]['label']='X'*100
        with self.assertRaises(ValueError):
            diagram.render(self.spec)


class QueueTests(WorkspaceTest):
    def manifest(self,code="print('ok')",timeout=10):
        return self.write('jobs.json',json.dumps({'schema':'local-queue-v1','jobs':[{'id':'one','argv':[sys.executable,'-c',code],'timeout_seconds':timeout}]}))
    def test_dry_run_launches_nothing(self):
        m=self.manifest("from pathlib import Path; Path('marker').write_text('bad')")
        result=queue.run_queue(m,self.path/'state.json')
        self.assertEqual(result['status'],'DRY_RUN')
        self.assertFalse((self.path/'marker').exists())
        self.assertFalse((self.path/'state.json').exists())
    def test_resume_does_not_launch_twice(self):
        m=self.manifest("from pathlib import Path; p=Path('counter'); p.write_text(p.read_text()+'x' if p.exists() else 'x')")
        state=self.path/'state.json'
        first=queue.run_queue(m,state,True)
        second=queue.run_queue(m,state,True)
        self.assertEqual(first['jobs']['one']['status'],'succeeded')
        self.assertEqual(second['jobs']['one']['attempts'],1)
        self.assertEqual((self.path/'counter').read_text(),'x')
    def test_failed_job_not_automatically_retried(self):
        m=self.manifest('raise SystemExit(4)')
        state=self.path/'state.json'
        queue.run_queue(m,state,True)
        result=queue.run_queue(m,state,True)
        self.assertEqual(result['jobs']['one']['returncode'],4)
        self.assertEqual(result['jobs']['one']['attempts'],1)
    def test_changed_manifest_rejected(self):
        m=self.manifest()
        state=self.path/'state.json'
        queue.run_queue(m,state,True)
        self.manifest("print('new')")
        with self.assertRaises(ValueError):
            queue.run_queue(m,state,True)
    def test_ambiguous_launch_is_not_retried(self):
        m=self.manifest()
        state=self.path/'state.json'
        result=queue.run_queue(m,state,True)
        result['jobs']['one']['status']='running'
        state.write_text(json.dumps(result))
        with self.assertRaises(ValueError):
            queue.run_queue(m,state,True)
    def test_existing_lock_prevents_launch(self):
        m=self.manifest()
        self.write('state.json.lock','owner')
        with self.assertRaises(ValueError):
            queue.run_queue(m,self.path/'state.json',True)
        self.assertEqual((self.path/'state.json.lock').read_text(),'owner')
    def test_timeout_stays_unknown(self):
        m=self.manifest('import time; time.sleep(5)',0.05)
        state=self.path/'state.json'
        result=queue.run_queue(m,state,True)
        self.assertEqual(result['jobs']['one']['status'],'unknown')
        with self.assertRaises(ValueError):
            queue.run_queue(m,state,True)


class DebtTests(WorkspaceTest):
    def test_skip_dependencies_and_keep_line_numbers(self):
        self.write('app.py','# first\n# shortcut: max 100 rows\n')
        self.write('node_modules/lib.js','// shortcut: dependency\n')
        findings=debt.scan(self.path)
        self.assertEqual(len(findings),1)
        self.assertEqual(findings[0]['line'],2)
        self.assertEqual(findings[0]['status'],'UNTRIAGED')


class RepositoryTests(WorkspaceTest):
    def test_structure(self):
        result=validator.validate()
        self.assertEqual(result['errors'],[])
    def test_package_is_self_contained_and_hashed(self):
        archive=self.path/'plugin.zip'
        packager.package(archive)
        with zipfile.ZipFile(archive) as bundle:
            names=bundle.namelist()
            self.assertIn('.claude-plugin/plugin.json',names)
            self.assertIn('.claude-plugin/marketplace.json',names)
            self.assertEqual(sum(n.endswith('/SKILL.md') for n in names),69)
            self.assertFalse(any('.validation-deps' in n for n in names))
            manifest=json.loads(bundle.read('PACKAGE_CHECKSUMS.json'))
            for name,digest in manifest.items():
                self.assertEqual(hashlib.sha256(bundle.read(name)).hexdigest(),digest)


if __name__=='__main__':
    unittest.main()
