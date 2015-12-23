#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
"""

from nose.tools import *

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


class Test{{ cookiecutter.project_slug|capitalize }}:

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        print("test")
        assert_equal(1, 2)
