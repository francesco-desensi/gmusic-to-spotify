#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='gmusic_to_spotify',
    version='0.1.0',
    description="A tool for importing your existing google music playlists into Spotify.",
    long_description=readme + '\n\n' + history,
    author="Francesco DeSensi",
    author_email='desensif@gmail.com',
    url='https://github.com/francesco-desensi/gmusic_to_spotify',
    packages=[
        'gmusic_to_spotify',
    ],
    package_dir={'gmusic_to_spotify':
                 'gmusic_to_spotify'},
    entry_points={
        'console_scripts': [
            'gmusic_to_spotify=gmusic_to_spotify.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='gmusic_to_spotify',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
