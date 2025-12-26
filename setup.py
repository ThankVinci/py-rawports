from setuptools import setup
from setuptools.command.bdist_wheel import bdist_wheel
import os

version = os.getenv('PKG_VERSION', '0.0.1a0')
py_tag = os.getenv('PYTHON_TAG', 'py38')

class BDistWheelWithTag(bdist_wheel):
    def initialize_options(self):
        super().initialize_options()
        self.python_tag = py_tag

setup(version=version, 
      cmdclass={
        'bdist_wheel': BDistWheelWithTag,
        }
    )
