============
Installation
============

Requirements:
  - python >= 2.7

You can install, upgrade, uninstall {{ cookiecutter.repo_name }} with these commands::

  $ pip install [--user] {{ cookiecutter.repo_name }}
  $ pip install [--user] --upgrade {{ cookiecutter.repo_name }}
  $ pip uninstall {{ cookiecutter.repo_name }}

Or from git (last development version)::

  $ pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git

Or if you already pulled the sources::

  $ pip install path/to/sources

Or if you don't have pip::

  $ easy_install {{ cookiecutter.repo_name }}
