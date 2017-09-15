from __future__ import absolute_import

from setuptools import find_packages
from setuptools import setup

setup(
    name='check_grgen',
    description='pre-commit hook for validation of grgen files',
    url='https://github.com/balrok/check-grgen',
    version='1.0',
    author='Carl Mai',
    author_email='carl.schoenbach@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
    ],
    extras_require={
        'dev': [
            'pre-commit',
        ]
    },
    entry_points={
        'console_scripts': [
            'check-grgen= check_grgen.main:main',
        ],
    },
)

