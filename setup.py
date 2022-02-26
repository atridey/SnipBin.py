"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='SnipBin.py',
    version='1.0.1.3',
    description='A Python API wrapper for SnipBin (http://snip.hxrsh.in/)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/airD173/SnipBin.py',
    author='Atri Dey',
    author_email='adey1731@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='api, wrapper, paste, snipbin',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['requests'],
    project_urls={
        'Bug Reports': 'https://github.com/airD173/SnipBin.py/issues',
    },
)
