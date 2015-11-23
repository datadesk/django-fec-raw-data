import os
from setuptools import setup


setup(
    name='django-fec-raw',
    version='0.1',
    packages=['fec_raw'],
    include_package_data=True,
    license='MIT',  # example license
    description='A simple Django app to conduct Web-based polls.',
    author='The Los Angeles Times Data Desk',
    author_email='datadesk@latimes.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires = [
        'django-postgres-copy>=0.0.6',
        'feedparser>=5.2.1',
        'tomorrow>=0.2.3',
    ]
)
