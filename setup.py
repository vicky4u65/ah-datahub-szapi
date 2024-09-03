"""Python setup.py for ah_datahub_szapi package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("ah_datahub_szapi", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ah_datahub_szapi",
    version=read("ah_datahub_szapi", "VERSION"),
    description="Awesome ah_datahub_szapi created by vicky4u65",
    url="https://github.com/vicky4u65/ah-datahub-szapi/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="vicky4u65",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["ah_datahub_szapi = ah_datahub_szapi.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
