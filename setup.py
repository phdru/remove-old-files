#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import setup
import sys

if sys.version_info[:2] == (2, 7):
    from imp import load_source

elif sys.version_info >= (3, 4):
    from importlib.machinery import SourceFileLoader
    import types

    def load_source(fullname, path):
        loader = SourceFileLoader(fullname, path)
        loaded = types.ModuleType(loader.name)
        loader.exec_module(loaded)
        return loaded

else:
    raise ImportError("ppu requires Python 2.7 or 3.4+")

versionpath = join(abspath(dirname(__file__)), "ppu", "__version__.py")
ppu_version = load_source("ppu_version", versionpath)

setup(
    name='ppu',
    version=ppu_version.__version__,
    description='Broytman Portable Python Utilities',
    long_description=open('README.rst', 'rU').read(),
    long_description_content_type="text/x-rst",
    author='Oleg Broytman',
    author_email='phd@phdru.name',
    url='https://phdru.name/Software/Python/ppu/',
    project_urls={
        'Homepage': 'https://phdru.name/Software/Python/ppu/',
        'Documentation': 'https://phdru.name/Software/Python/ppu/docs/',
        'Download': 'https://pypi.org/project/ppu/%s/'
        % ppu_version.__version__,
        'Git repo': 'https://git.phdru.name/ppu.git/',
        'Github repo': 'https://github.com/phdru/ppu',
        'Issue tracker': 'https://github.com/phdru/ppu/issues',
    },
    license='GPL',
    platforms='Any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['ppu'],
    scripts=[
        'scripts/cmp.py', 'scripts/remove-old-files.py', 'scripts/rm.py',
        'scripts/which.py',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
)
