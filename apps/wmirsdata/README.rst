***************************
CAP NASA Weather WMIRS Data
***************************



Docker Steps
============

The simplest method to executing this process, regardless of OS, is to use
`Docker <https://www.docker.com>`_; because it only requies the installation
of one cross platform application and the setup of a set of directories.

#. Install `Docker Desktop <https://www.docker.com/products/docker-desktop/>`_.

   #. The docker desktop personal plan will be used at no cost.

   #. On above website scroll to `Download Docker Desktop` button and choose
      the version for the operating system you are using.

#. Create three directories: `data/in`, `data/out`, `data/err`.

#. Change to the data directory.

#. Put files to be validated and transformed into `data/in`.

#. Run command

::

   docker run --rm \
   --volume=${PWD}/in:/var/lib/wmirsdata/in \
   --volume=${PWD}/out:/var/lib/wmirsdata/out \
   --volume=${PWD}/err:/var/lib/wmirsdata/err \
   wmirsdata

#. Files validated and transformed will be in `data/out`, both the original
   file (which is moved), and the transformed file with a json extension.

#. Files that contained errors will be in `data/err`, both the original file
   and a log file that explains each of the errors.



Local Usage
===========

If you would rather work with the source code and have more options availble,
then this section is for you.


Prerequisites
-------------

#. Required packages:

   #. `Python <https://www.python.com>`_
   #. `pip <https://pip.pypa.io/en/stable/>`_
   #. `Task (aka Taskfile) <https://taskfile.dev>`_
   #. `pre-commit <https://pre-commit.com>`_

#. Recommended packages:

   #. `virtualenv <https://virtualenv.pypa.io/en/latest/>`_
   #. `direnv <https://direnv.net>`_

#. Optional packages (required for some development tasks):

   #. `Docker engine <https://www.docker.com>`_
   #. `act <https://nektosact.com>`_


Setup
-----

#. Clone this repository.

#. Create and activate a virtual environment.

   #. ``python -m venv .venv``
   #. ``source .venv/bin/activate``

#. Run ``task setup:dev`` which will get all necessary python packages, setup
   git hooks, and any other setup necessary to run locally.

#. Run ``task build`` to build the application locally.

#. Run ``task tests`` to run all the tests against the build.

#. To execute the application use the command ``wmirsdata``, to get help and
   see actions use ``wmirsdata --help``.



Development
===========

If you would like to aid in development this section is for you.


Process
-------

#. Make changes in a local git branch. If the change is associated with an
   issue (recommended but not required) then the branch should have been
   created from the issue itself.

#. Push the branch to GitHub.

#. Open a pull request.


Task
----

[Task](https://taskfile.dev) is a task runner and build tool that is easier
to use than `make`. The main file is `Taskfile.dist.yml` which contains
various tasks that could be used in working with carbon.

The runtime environment for task starts with the shell environment. Then
either the `${PWD}/.env` or `${HOME}/.env` will be sourced (if exists).
These files should contain your configuration, keys, passwords, etc. that
should not be committed to the repo and are required by specific tasks.


direnv
------

It is recommended that `direnv` be installed and a `.envrc` file be created
in the local clone of the repository. This can handle setting the environment
when changing into the directory, and if a virtual environment is not
available, creating a new one so `task setup:dev` may be run.


pre-commit
----------

The [pre-commit](https://pre-commit.com) framework will check any changed
file for conformance to coding standards, formatting standards, and security
standards before allowing a commit to occur.

Each of these checks are done in GitHub Actions as part of the CI/CD chain.
So having pre-commit perform these checks before commit improves the chances
that a PR will pass its checks.
