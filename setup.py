from setuptools import setup
import os

version = os.getenv('PKG_VERSION', '0.0.1a0')
setup(version=version)