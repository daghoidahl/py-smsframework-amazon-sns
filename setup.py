#! /usr/bin/env python
""" SMS framework: Amazon SNS provider """

from setuptools import setup, find_packages

setup(
    # http://pythonhosted.org/setuptools/setuptools.html
    name='smsframework-amazon-sns',
    version='0.0.2',
    author='Mark Vartanyan',
    author_email='kolypto@gmail.com',

    url='https://github.com/kolypto/py-smsframework-amazon-sns',
    license='BSD',
    description=__doc__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['sms', 'message', 'notification', 'receive', 'send', 'amazon', 'sns'],

    packages=find_packages(),
    scripts=[],
    entry_points={},

    install_requires=[
        'smsframework >= 0.0.9',
        'boto3 >= 1.4'
    ],
    extras_require={
        'receiver': ['flask >= 0.10'],  # sms receiving
    },
    test_suite='nose.collector',
    include_package_data=True,

    platforms='any',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
)
