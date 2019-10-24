"""A setuptools based setup module for Mini_CSV_Wrangler_TakeHomeTest"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'click',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Mini_CSV_Wrangler_TakeHomeTest',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="This is a mini csv wrangler that reads a configdata.txt and transformation the provided source csv to and out csv as per the requirement",
    long_description=readme + '\n\n' + history,
    author="Ankita Sharma",
    author_email='ankita.sharma46@gmail.com',
    url='https://github.com/Ankita0105/Mini_CSV_Wrangler_TakeHomeTest',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts':[
            'Mini_CSV_Wrangler_TakeHomeTest=Mini_CSV_Wrangler.CSV_wrangler:wrangleCSV',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
