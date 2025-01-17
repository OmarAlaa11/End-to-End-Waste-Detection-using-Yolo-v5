'''
Purpose of the setup.py File:
Packaging: Prepares your project to be installed as a Python package.
'''
from setuptools import find_packages, setup

setup(
    name = 'WasteDetection',
    version= '0.0.0',
    author= 'Omar Alaa',
    author_email= 'omaralaa@gmail.com',
    packages= find_packages(), #Automatically finds and includes all Constructor files in the current directory and subdirectories (that contain an __init__.py file).
    install_requires = []
)