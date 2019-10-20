from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="passfactory",
    version="1.0",
    description="A random password generator which includes various utils to work with them",
    py_modules=["passgen"],
    package_dir={"":"src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tester86/passfactory",
    author="Tester86",
    author_email="tester86t@gmail.com",
)