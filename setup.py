#!/usr/bin/env python
from setuptools import find_packages, setup


project = "puffpastry"
version = "0.1.0"


setup(
    name=project,
    version=version,
    description="puffpastry - lightweight dependency injection for Python",
    author="puffpastry",
    author_email="adamhadani@gmail.com",
    url="https://github.com/adamhadani/puffpastry",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "python-dotenv",
    ],
    extras_require={
        "lint": [
            "black>=23.9.1",
            "flake8>=6.1.0",
            "flake8-bugbear>=23.9.16",
        ],
        "test": [
            "coverage>=7.3.1",
            "pytest>=7.4.2",
            "pytest-cov>=4.1.0",
        ],
    },
)
