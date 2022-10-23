import os
from setuptools import find_packages
from numpy.distutils.core import setup

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    install_requires=install_requires,
    package_dir={"":"src"},
    packages=find_packages(where="src")
)
