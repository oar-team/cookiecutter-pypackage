#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

test_{{ cookiecutter.package_name }}
----------------------------------

Tests for `{{ cookiecutter.package_name }}` module.
"""

import unittest

from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name }}


class Test{{ cookiecutter.package_name | replace("_", " ") | title | replace(" ", "") }}(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass
