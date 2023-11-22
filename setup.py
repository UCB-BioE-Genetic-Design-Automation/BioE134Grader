from setuptools import setup, find_packages

setup(
    name='BioE134Grader',
    version='0.1.0',
    author='J. Christopher Anderson',
    author_email='jcanderson@berkeley.edu',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        # For example: 'numpy', 'pandas'
    ],
    description='An autograder library for BioE134 course.'
)
