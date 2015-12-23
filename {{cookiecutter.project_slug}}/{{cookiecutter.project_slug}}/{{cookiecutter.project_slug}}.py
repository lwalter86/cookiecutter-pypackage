#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
{{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}
"""


def add(a, b):
    """
    Example add function with docstring and doctest

    Parameters
    ----------
    a : int
        Number
    b : int
        Number

    Returns
    -------
    result : sum of ``a`` and ``b``


    >>> add(3, 2)
    5
    """
    return a + b

def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
