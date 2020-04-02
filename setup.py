import numpy
from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    # Basic info
    name="operation_benchmarking",
    # version=version,
    author="Onur Solmaz",
    author_email="onur@casperlabs.io",
    url="",
    description="",
    # long_description='',
    classifiers=[],
    # Packages and depencies
    # package_dir={'': 'highway_economic_simulator'},
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    # packages=find_packages('highway_economic_simulator'),
    install_requires=["numpy", "scipy", "cython", "progressbar2", "sortedcontainers",],
    ext_modules=cythonize("operation_benchmarking/*.pyx"),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
    platforms="any",
)
