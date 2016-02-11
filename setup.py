#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='django-fec-raw-data',
    version='0.0.3',
    packages=(
        'fec_raw',
        'fec_raw.management',
        'fec_raw.management.commands',
        'fec_raw.models',
    ),
    include_package_data=True,
    license='MIT',
    description='A Django app to download, extract and load campaign finance from the Federal Election Commission',
    author='The Los Angeles Times Data Desk',
    author_email='datadesk@latimes.com',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    install_requires=(
        'django-postgres-copy>=0.0.6',
        'feedparser>=5.2.1',
        'tomorrow>=0.2.3',
    )
)
