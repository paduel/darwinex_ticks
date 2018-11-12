import io
import os
from setuptools import setup, find_packages

DESCRIPTION = 'Darwinex tick data downloader Python API'
here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(
    name='darwinex_ticks',
    version='0.0.4',
    packages=['pandas'],
    url='https://github.com/paduel/darwinex_ticks',
    license='MIT',
    author='Paduel',
    author_email='paduel@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=['pandas'],
    extras_require={'progress bar': ['ipywidgets']},
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

)
