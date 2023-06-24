from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="even-dist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src", include=["*"]),
    package_dir={"": "src"},
    package_data={"hello": ["*.txt"]},
    include_package_data=True,
    version="0.3.1",
    description="My first Python library",
    install_requires=["numpy", "matplotlib"],
    author="kirp",
    author_email="kirp@umich.edu",
    license="MIT",
    setup_requires=["pytest-runner"],
    test_suite="tests",
    url="https://github.com/tic-top/even_dist/",
)
