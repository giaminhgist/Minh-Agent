# Notification integration

This is an adapter contract for the source feishu-notify capability, not an installed webhook service. No notifications are sent on plugin installation or task completion by default.

Before a send, resolve explicit user authorization, destination, permitted content and the configured connector. Prepare a payload with event ID, project/run ID, concise status, timestamp and artifact link. Do not include secrets, full logs or private manuscript content unless requested and appropriate for the destination.

Use the connector's real delivery result. Persist a delivery identifier when available; do not retry an ambiguous send blindly. For interactive questions, only a verified reply from the intended user is an answer. Timeout is not approval. A failed notification must not change experiment or review status.

For Feishu/Lark, use a supported connector or a reviewed backend implementation and its current authentication/signature contract. No SDK/webhook implementation is included in v0.1.0. Runtime status: NOT_RUN. A draft payload can be delivered locally when no sending capability exists, explicitly labeled unsent.
