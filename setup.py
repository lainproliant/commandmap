from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="commandmap",
    version="1.0.0",
    description="A small module for mapping commands onto object methods by prefix.",
    url="https://github.com/lainproliant/commandmap",
    author="Lain Musgrove (lainproliant)",
    author_email="lainproliant@gmail.com",
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="mapping commands cli",
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    package_data={"commandmap": ["LICENSE"]},
    data_files=[],
    entry_points={"console_scripts": []},
)
