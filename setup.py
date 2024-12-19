from setuptools import setup, find_packages

setup(
    name="library_management",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
    ],
) 