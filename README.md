# REST API client for gitlab servers

## Bugs and gotchas

1. while creating a user, the `confirm` flag is ignored;

2. if you use file-level commands (such as `rsync`, `cpio`, etc.) for copying content of a git repository,
it should be done after creation a `project` the repository belongs to, not before.