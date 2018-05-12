from setuptools import setup, find_packages

__version__ = None  # Avoids IDE errors, but actual version is read from version.py
exec (open('botsociety/version.py').read())

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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    version=__version__,
    install_requires=install_requires,
    tests_require=tests_requires,
    include_package_data=True,
    description="Client to connect to Botsociety",
    author='Rasa Technologies',
    author_email='tom@rasa.com',
    url="https://rasa.com",
    keywords=["botsociety", "bots", "dialogue"]
)
