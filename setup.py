import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plantwatering",
    version="0.0.1",
    author="Bob",
    author_email="bob.ebarnhart@gmail.com",
    description="A package used to water plants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/algobar/plant-watering",
    package_dir={"": "."},
    packages=find_packages(where="."),
    python_requires=">=3.8",
)
