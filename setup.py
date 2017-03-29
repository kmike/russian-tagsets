#! /usr/bin/env python
import platform
from distutils.core import setup

try:
    import __pypy__
except ImportError:
    __pypy__ = None

__version__ = '0.5.2'
py2 = int(platform.python_version_tuple()[0]) == 2

if __pypy__ or py2:
    ld1 = open('README.rst').read()
    ld2 = open('CHANGES.rst').read()
else:
    ld1 = open('README.rst', encoding='utf-8').read()
    ld2 = open('CHANGES.rst', encoding='utf-8').read()

setup(
    name="russian-tagsets",
    version=__version__,
    description="Russian tagset converters library",
    long_description = ld1 + "\n\n" + ld2,
    license = 'MIT license',
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    url = 'https://github.com/kmike/russian-tagsets/',

    packages = ['russian_tagsets', 'russian_tagsets.positional'],

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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],

)




