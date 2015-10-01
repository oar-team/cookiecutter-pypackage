#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import os.path as op


from codecs import open
from setuptools import setup, find_packages


def read(fname):
    ''' Return the file content. '''
    here = op.abspath(op.dirname(__file__))
    with open(op.join(here, fname), 'r', 'utf-8') as fd:
        return fd.read()

readme = read('README.rst')
changelog = read('CHANGES.rst').replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

if sys.version_info[0] == 2:
    # TODO: put python2-only package requirements
    # requirements.append('example-package')
    pass

version = ''
version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                    read(op.join('{{ cookiecutter.package_name }}', '__init__.py')),
                    re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


setup(
    name='{{ cookiecutter.repo_name }}',
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    version=version,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + changelog,
    keywords='{{ cookiecutter.repo_name }}',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
    ],
)
