#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

import argparse

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file', default='')
    args = parser.parse_args()

    logger.info(args)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
