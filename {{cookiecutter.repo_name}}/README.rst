===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/

.. image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/

.. image:: https://img.shields.io/pypi/status/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/

.. image:: https://img.shields.io/pypi/dm/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/

.. image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements.svg?branch=master
        :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/requirements/?branch=master

.. image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master/landscape.svg?style=flat
        :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/master

.. image:: https://www.codacy.com/project/badge/BADGEID
        :target: https://www.codacy.com/app/s-celles/{{ cookiecutter.repo_name }}/

.. image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest
        :target: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/


{{ cookiecutter.project_short_description}}

* Documentation: https://{{ cookiecutter.project_slug }}.readthedocs.org.

Features
--------

* TODO

Install
-------

.. code:: bash

    $ pip install {{ cookiecutter.project_slug }}

Usage
-----

.. code:: python

    In [1]: from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

Development
-----------

You can help to develop this library.

Issues
^^^^^^

You can submit issues using https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues

Clone
^^^^^

You can clone repository to try to fix issues yourself using:

::

    $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

Run unit tests
^^^^^^^^^^^^^^

Run all unit tests

::

    $ nosetests -s -v --with-doctest

Run a given test

::

    $ nosetests tests/test_{{ cookiecutter.project_slug }}.py:{{ cookiecutter.project_slug|capitalize }}.test_000_something -s -v

Install development version
^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ python setup.py install

or

::

    $ sudo pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

Collaborating
^^^^^^^^^^^^^

-  Fork repository
-  Create a branch which fix a given issue
-  Submit pull requests

https://help.github.com/categories/collaborating/

Examples
^^^^^^^^

see `samples <samples>`_ directory

Credits
---------

This package was created with Cookiecutter_ and the `{{ cookiecutter.github_username }}/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`{{ cookiecutter.github_username }}/cookiecutter-pypackage`: https://github.com/{{ cookiecutter.github_username }}/cookiecutter-pypackage
