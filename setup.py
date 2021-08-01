import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plant-watering",
    version="0.0.1",
    author="Bob",
    author_email="bob.ebarnhart@gmail.com",
    description="A package used to water plants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/algobar/plant-watering",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)