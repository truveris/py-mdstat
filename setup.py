# Copyright 2015-2016, Truveris Inc. All Rights Reserved.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="mdstat",
    version="1.0.4",
    description="mdstat parser",
    author="Truveris Inc.",
    author_email="dev@truveris.com",
    url="https://github.com/truveris/py-mdstat/",
    license="MIT License",
    keywords=["linux", "mdstat", "mdadm", "mdjson","raid"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    scripts=[
        "tools/mdjson",
    ],
    test_suite="nose.collector",
    packages=["mdstat"],
)
