#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-wiki-blackcrystal",
    version="0.0.1",
    author="Sergei Miami",
    author_email="miami@blackcrystal.net",
    description="Wiki pages in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlackCrystal/python-wiki",
    project_urls={
        "Bug Tracker": "https://github.com/BlackCrystal/python-wiki/issues",
        "Project": "https://github.com/BlackCrystal/python-wiki/projects/1",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
