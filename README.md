# REST API client for gitlab servers

## Configuration files

URLs and private tokens for all the gitlab servers you're working with (a.k.a. 'systems') should be placed in the `~/.gitlab_systems.json`
(this file must be readable and writable only by its owner). Example of its content could be found [here](dot.gitlab_systems.sample.json).
Gitlab users whose tokens are saved in this file have to have permissions to do all the things you're planning to do by this client 
on the particulary server.

## Documentation

Gitlab's REST API is pretty well documented [here](https://github.com/gitlabhq/gitlabhq/tree/master/doc/api).

## Bugs and gotchas

1. while creating a user, the `confirm` flag is ignored;

2. if you use file-level commands (such as `rsync`, `cpio`, etc.) for copying content of a git repository,
it should be done after creation a `project` the repository belongs to, not before.