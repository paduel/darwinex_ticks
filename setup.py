from setuptools import setup, find_packages

DESCRIPTION = 'Darwinex tick data downloader Python API'

try:
    with open('README.md') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name='Darwinex-ticks',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/paduel/darwinex_ticks',
    license='MIT',
    author='Paduel',
    author_email='paduel@gmail.com',
    install_requires=['pandas'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
)
