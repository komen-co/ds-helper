from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.exceptions import InstallationError

try:
    requirements = parse_requirements("requirements.txt")
    install_requires = [str(r.req) for r in requirements]
except InstallationError:
    install_requires = []

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="ds-helper-py",
    version="1.0.0",
    description="basic package",
    license="MIT",
    author="Komenco",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description
)
