from setuptools import setup

#from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
   author = "Andrew Miller",
   name = 'pydtw',
   license = "MIT",
   packages = ['pydtw'],
   ext_modules  = cythonize(['pydtw/*.pyx']),
   include_dirs = [numpy.get_include(),],
)

