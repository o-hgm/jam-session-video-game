#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='jam-session-pygame',
      version='0.0.1',
      description='A Jam Session',
      author='None',
      author_email='foo@bar.xyz',
      url='https://www.github.com/',
        packages=find_packages(),
    entry_points = {
        'console_scripts': ['jam-session=jam_session.bin.cli:main'],
    }
)