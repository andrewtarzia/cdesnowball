#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = '''A toolkit for extracting chemical information from the scientific literature.'''

setup(
    name='ChemDataExtractor-Snowball',
    version='1.4',
    author='Callum Court',
    author_email='cc889@cam.ac.uk',
    license='MIT',
    url='https://github.com/cjcourt/cdesnowball',
    packages=find_packages(),
    description='A toolkit for extracting chemical information from the scientific literature.',
    long_description=long_description,
    keywords='text-mining mining chemistry cheminformatics nlp html xml science scientific',
    zip_safe=False,
    entry_points={'console_scripts': ['cde = chemdataextractor_snowball.cli:cli']},
    tests_require=['pytest'],
    install_requires=[
        'appdirs', 'beautifulsoup4', 'click', 'cssselect', 'lxml', 'nltk', 'pdfminer.six', 'python-dateutil',
        'requests', 'six', 'python-crfsuite', 'DAWG', 'PyYAML'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
