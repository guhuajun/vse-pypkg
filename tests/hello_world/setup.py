# A setuptools based setup module.
# See:
# https://packaging.python.org/en/latest/distributing.html
# https://github.com/pypa/sampleproject

from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='sample',
    version='1.2.0',


    description='A sample Python project',
    long_description=long_description,
    url='https://github.com/pypa/sampleproject',


    author='The Python Packaging Authority',
    author_email='pypa-dev@googlegroups.com',


    license='MIT',


    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='sample setuptools development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),


    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],


    # install_requires=['peppercorn'],


    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },


    # package_data={
    #     'sample': ['package_data.dat'],
    # },


    # data_files=[('my_data', ['data/data_file'])],


    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)