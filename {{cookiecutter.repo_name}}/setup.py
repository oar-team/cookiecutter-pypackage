#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
history = read('HISTORY.rst').replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

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
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    keywords='{{ cookiecutter.repo_name }}',
    license="GNU GPL",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering',
    ],
)
