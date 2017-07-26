from setuptools import setup

#from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
   name = "Andrew Miller",
   license = "MIT",
   packages = ['pydtw'],
   ext_modules  = cythonize(['pydtw/*.pyx']),
   include_dirs = [numpy.get_include(),],
)

