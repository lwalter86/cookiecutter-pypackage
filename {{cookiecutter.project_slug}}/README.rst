===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/

.. image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/

.. image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/

.. image:: https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/

.. image:: https://img.shields.io/pypi/status/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/

.. image:: https://img.shields.io/pypi/dm/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/

.. image:: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/requirements.svg?branch=master
        :target: https://requires.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/requirements/?branch=master

.. image:: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/master/landscape.svg?style=flat
        :target: https://landscape.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/master

.. image:: https://www.codacy.com/project/badge/BADGEID
        :target: https://www.codacy.com/app/s-celles/{{ cookiecutter.project_slug }}/

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
        :target: https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/


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

You can submit issues using https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/issues

Clone
^^^^^

You can clone repository to try to fix issues yourself using:

::

    $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git

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

    $ sudo pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git

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
