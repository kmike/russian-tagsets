#! /usr/bin/env python
import sys
from setuptools import setup

__version__ = '0.6'
PY2 = sys.version_info[0] == 2

if PY2:
    ld1 = open('README.rst').read()
    ld2 = open('CHANGES.rst').read()
else:
    ld1 = open('README.rst', encoding='utf-8').read()
    ld2 = open('CHANGES.rst', encoding='utf-8').read()

setup(
    name="russian-tagsets",
    version=__version__,
    description="Russian tagset converters library",
    long_description=ld1 + "\n\n" + ld2,
    license='MIT license',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    url='https://github.com/kmike/russian-tagsets/',
    packages=['russian_tagsets', 'russian_tagsets.positional'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],

)




