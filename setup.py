import io
import os
from setuptools import setup

DESCRIPTION = 'Darwinex tick data downloader Python API'
here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(
    name='Darwinex-ticks',
    version='0.0.4',
    packages=['darwinex_ticks'],
    url='https://github.com/paduel/darwinex_ticks',
    license='MIT',
    author='Paduel',
    author_email='paduel@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
)
