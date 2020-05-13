from setuptools import setup, find_packages

# import numpy
# from Cython.Build import cythonize

setup(
    # Basic info
    name="opbench",
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
            "opbench_batch_fit=opbench.bin.opbench_batch_fit:main",
            "opbench_round_results=opbench.bin.opbench_round_results:main",
        ]
    },
    zip_safe=False,
    platforms="any",

    # ext_modules=cythonize("opbench/*.pyx"),
    # include_dirs=[numpy.get_include()],
)
