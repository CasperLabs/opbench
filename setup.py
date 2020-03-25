import os

from setuptools import setup, find_packages

dirname = os.path.dirname(__file__)


setup(
    # Basic info
    name="operation_costing",
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
    install_requires=[
        "numpy",
        "progressbar2",
        "sortedcontainers",
    ],
    zip_safe=False,
    platforms="any",
)
