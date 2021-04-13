import re

from setuptools import find_packages, setup

with open("README.md") as file:
    read_me_description = file.read()

with open("requirements.txt") as r:
    requirements = [i.strip() for i in r]

with open("aiotdlib/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

setup(
    name="aiotdlib",
    version=version,
    license='MIT',
    author="Pylakey",
    author_email="pylakey@protonmail.com",
    description="Python asyncio wrapper for TDLib",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    packages=find_packages(
        exclude=('generator',)
    ),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=3.9',
    include_package_data=True,
)
