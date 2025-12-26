from setuptools import setup
from setuptools.command.bdist_wheel import bdist_wheel
import os

class BDistWheelWithTag(bdist_wheel):
    def get_tag(self):
        python = "py38"
        abi = "none"
        plat = "any" # self.plat_name
        return python, abi, plat

version = os.getenv('PKG_VERSION', '0.0.1a0')
setup(version=version, 
      cmdclass={
        'bdist_wheel': BDistWheelWithTag,
        }
    )
