import io
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

# Avoids IDE errors, but actual version is read from version.py
__version__ = None
exec (open('botsociety/version.py').read())

# Get the long description from the README file
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

tests_requires = [
    "pytest-pep8",
    "pytest-services",
    "pytest-cov",
]

install_requires = [
    "requests",
]


setup(
    name='botsociety-client',
    packages=find_packages(exclude=["tests", "tools"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
    ],
    version=__version__,
    install_requires=install_requires,
    tests_require=tests_requires,
    include_package_data=True,
    description="Client to connect to Botsociety",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rasa Technologies GmbH',
    author_email='hi@rasa.com',
    maintainer="Tom Bocklisch",
    maintainer_email="tom@rasa.com",
    license='Apache 2.0',
    url="https://rasa.com",
    keywords=["botsociety", "bots", "dialogue"],
    download_url="https://github.com/RasaHQ/botsociety-py-client/archive/{}.tar.gz"
                 "".format(__version__),
    project_urls={
        'Bug Reports': 'https://github.com/RasaHQ/botsociety-py-client/issues',
        'Source': 'https://github.com/RasaHQ/botsociety-py-client',
    },
)
