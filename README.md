# REST API client for gitlab servers

This is gitlab REST API client library written in Python (currenty tested against `Python 2.7.8 [GCC 4.9.2 20141101 (Red Hat 4.9.2-1)]`).
It supports working with the following kinds of gitlab objects:

* branches
* groups
* projects
* users

[copyGroup.py](copyGroup.py) is a sample script using this library to copy a group with all the including members and repositories from one gitlab server to another.

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