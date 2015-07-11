# Copyright 2015, Truveris Inc. All Rights Reserved.

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name="mdstat",
    version="1.0.0",
    description="mdstat parser",
    author="Truveris Inc.",
    author_email="dev@truveris.com",
    url="https://truveris.com/",
    license="MIT License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    scripts=[
        "tools/mdjson",
    ],
    test_suite="nose.collector",
    packages=find_packages(exclude=["ez_setup"]),
)
