from setuptools import setup, find_packages

# import numpy
# from Cython.Build import cythonize

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
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=[
        "numpy",
        "scipy",
        "cython",
        "progressbar2",
        "sortedcontainers",
        "toml",
    ],
    entry_points={
        "console_scripts": [
            "ob_batch_fit=operation_benchmarking.bin.ob_batch_fit:main",
            "ob_round_results=operation_benchmarking.bin.ob_round_results:main",
        ]
    },
    zip_safe=False,
    platforms="any",

    # ext_modules=cythonize("operation_benchmarking/*.pyx"),
    # include_dirs=[numpy.get_include()],
)
