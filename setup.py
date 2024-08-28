# setup.py

from setuptools import setup, find_packages

setup(
    name='irrelevant-content-detection',
    version='0.1',
    description='A Python package for detecting irrelevant content in texts.',
    author='Berk Birkan',
    author_email='info@berkbirkan.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'scipy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
