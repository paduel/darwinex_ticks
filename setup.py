import os
from setuptools import setup, find_packages

DESCRIPTION = 'Darwinex tick data downloader Python API'
# ere = os.path.abspath(os.path.dirname(__file__))

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name='Darwinex-ticks',
    version='0.0.9',
    packages=find_packages(),
    url='https://github.com/paduel/darwinex_ticks',
    license='MIT',
    author='Paduel',
    author_email='paduel@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['pandas'],
)
