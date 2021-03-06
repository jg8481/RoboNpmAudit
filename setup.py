from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RoboNpmAudit',
    version='1.0',
    packages=[''],
    package_dir={'': 'robonpmaudit'},
    url='https://www.github.com/we45/RoboNpmAudit',
    license='MIT',
    author='we45',
    author_email='info@we45.com',
    description='Robot Framework Library for NPM Audit Source Composition Analysis' ,
    install_requires=[
        'docker',
        'robotframework==3.0.4'
    ],
    long_description = long_description,
    long_description_content_type='text/markdown'
)
