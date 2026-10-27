# Minh-Agent Skills

Kho **69 Skills** cho coding và nghiên cứu, ưu tiên các workflow từ ARIS và superpowers. Bao gồm idea discovery, research/grant proposal, paper writing/revision, plots/diagrams/illustrations, experiments, proofs, patents và các tác vụ nghiên cứu chuyên sâu.

Một thư mục `skills/` là nguồn duy nhất cho hai cách cài: **plugin Claude Code** và **Skills cho Codex**. Phiên bản đầu: `0.1.0`.

## Cài cho Claude Code

Thêm marketplace từ GitHub repo [giaminhgist/Minh-Agent](https://github.com/giaminhgist/Minh-Agent) rồi cài plugin:

```sh
claude plugin marketplace add giaminhgist/Minh-Agent
claude plugin install minh-agent@minh-agent-marketplace
```

Hoặc trong phiên Claude Code:

```text
/plugin marketplace add giaminhgist/Minh-Agent
/plugin install minh-agent@minh-agent-marketplace
```

Repo phải ở chế độ public để Claude Code clone được; manifest nằm ở `.claude-plugin/plugin.json` và `.claude-plugin/marketplace.json` trên branch `main`.

Thử bản local chưa cần đăng ký marketplace:

```sh
claude --plugin-dir .
```

Hoặc thêm marketplace từ thư mục đã clone:

```sh
claude plugin marketplace add .
claude plugin install minh-agent@minh-agent-marketplace
```

Gọi một Skill, ví dụ:

```text
/minh-agent:idea-discovery Tìm hướng nghiên cứu khả thi với một GPU.
/minh-agent:grant-proposal Viết draft theo funding call tôi cung cấp.
/minh-agent:paper-figures Tạo biểu đồ từ results.csv và giữ source tái tạo.
```

## Cài cho Codex

Cần Python 3.10+; installer không cần thư viện ngoài. Chạy từ thư mục repo này, thay đường dẫn project bằng đường dẫn thật:

```sh
python tools/install.py --host codex --scope project --project "PATH_TO_PROJECT"
python tools/install.py --host codex --scope project --project "PATH_TO_PROJECT" --apply
```

Lệnh đầu chỉ liệt kê, lệnh có `--apply` mới cài vào `<project>/.agents/skills`. Để dùng cho mọi project:

```sh
python tools/install.py --host codex --scope user --apply
```

Phạm vi user dùng `~/.agents/skills`. Cài một nhóm hoặc một số Skills:

```sh
python tools/install.py --host codex --scope user --profile "Figures & communication" --apply
python tools/install.py --host codex --scope user --skills idea-discovery grant-proposal manuscript-writing --apply
```

Gọi `$idea-discovery`, `$grant-proposal`, `$paper-figures` hoặc mô tả tác vụ tự nhiên. Skills giữ automatic discovery mặc định; nếu host chưa nhận thay đổi, mở lại phiên. Installer từ chối ghi đè Skill khác tên trùng và giữ nguyên bản đã bị sửa. Để gỡ bản do installer cài, dùng cùng scope/selection với `--remove --apply`; nếu bản cài đã thay đổi, sao lưu và xử lý thủ công. Khi nâng cấp, gỡ bản cũ không bị sửa rồi cài bản mới. Không tự sửa cấu hình tài khoản hoặc cài dịch vụ.

OpenCode có tùy chọn `--host opencode` với cùng nội dung; discovery thực tế trên OpenCode chưa được kiểm thử trong phiên này.

## Chọn tác vụ và xem độ bao phủ

- [Catalog 69 Skills](CATALOG.md): nhóm, mục đích và đường dẫn.
- [Hướng dẫn sử dụng](docs/USAGE.md): luồng idea → proposal → experiment → paper → figures.
- [Độ bao phủ và giới hạn](docs/COVERAGE.md): mapping 113 entrypoint, khác biệt và backend còn thiếu.
- [Kiểm chứng đã chạy](docs/VALIDATION.md): phân biệt tests local, host integration và behavioral eval.
- [Tích hợp host](docs/host-integration.md), [notifications](docs/notification-integration.md), [catalog/benchmarks](docs/catalog-and-benchmarks.md).
- [Nguồn và license](THIRD_PARTY_NOTICES.md), [điều kiện phân phối](LICENSE).

## Trạng thái thực tế

Đã viết 69 workflow, refs, bốn helper chạy local, installer Codex/OpenCode và cấu trúc plugin/marketplace Claude Code. Mapping entrypoint đầy đủ **không đồng nghĩa full runtime parity**. Các helper local có phạm vi riêng: plot SVG cơ bản, diagram schema nhỏ, queue serial local và debt scanner. Provider adapters, full FigureSpec, forensic engine, cloud, Overleaf và mọi ARS schema chưa được port/kiểm chứng đầy đủ.

Hiện đây là bản phát triển dùng cá nhân, không tuyên bố production-ready. Toàn kho chưa có blanket license để public/commercial redistribution; giữ attribution và các điều kiện nguồn, đặc biệt ARS CC BY-NC 4.0.

## Kiểm tra và đóng gói

```sh
python tools/validate.py
python -m unittest discover -s tests -v
claude plugin validate .
python tools/package.py dist/minh-agent-0.1.0.zip
```

ZIP giữ nguyên cấu trúc repo và có checksum từng file. Giải nén trước khi thêm marketplace local. Lệnh Claude cần Claude Code CLI; validation offline của repo không thay thế validator đó.

Tài liệu host đã đối chiếu ngày 2026-10-27: [Claude plugins](https://code.claude.com/docs/en/plugins), [marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [Codex local skills](https://learn.chatgpt.com/docs/build-skills), [OpenCode skills](https://opencode.ai/docs/skills/).
