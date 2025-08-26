from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy
import sys
import platform

# Platform-specific compiler arguments
extra_compile_args = []
extra_link_args = []

if platform.system() == 'Windows':
    # Windows-specific settings
    extra_compile_args = ['/openmp'] if sys.platform == 'win32' else ['-fopenmp']
    extra_link_args = [] if sys.platform == 'win32' else ['-fopenmp']
else:
    # Unix-like systems
    extra_compile_args = ['-fopenmp']
    extra_link_args = ['-fopenmp']

# Define the Cython extension
extensions = [
    Extension(
        'cyext_acpi',
        ['acpi/cyext_acpi/cyext_acpi.pyx'],
        include_dirs=[numpy.get_include()],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        define_macros=[('CYTHON_TRACE_NOGIL', '1')]
    )
]

setup(
    name='acpi',
    version='0.1.0',
    packages=find_packages(),
    ext_modules=cythonize(extensions, compiler_directives={'linetrace': True, 'binding': True}),
    include_dirs=[numpy.get_include()],
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn',
        'cython',
        'tqdm'
    ],
    python_requires='>=3.7',
)