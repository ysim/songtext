#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

import libsongtext
version = '%s.%s.%s' % libsongtext.__version__

try:
    long_description = open('README.rst', 'U').read()
except IOError:
    long_description = 'See https://github.com/ysim/songtext'

setup(
    name='songtext',
    version=version,
    url='https://github.com/ysim/songtext',
    author='Yi Qing Sim',
    author_email='yq@yiqingsim.net',
    description='a command-line song lyric fetcher',
    long_description=long_description,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'songtext = libsongtext.songtext:main',
        ],
    },
    install_requires=[
        'click==6.7',
        'cssselect==1.0.1',
        'lxml==3.7.3',
        'requests==2.21.0',
    ],
    license='BSD',
    keywords='console command line music song lyrics',
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
