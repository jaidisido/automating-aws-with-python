# -*- coding: utf-8 -*-

"""Packaging configuration."""

from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Abdel Jaidi',
    author_email='aj@acloud.guru',
    description='Webotron is a tool to manage S3 buckets creation and configuration',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/jaidisido/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
