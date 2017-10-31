import os
# from pip.req import parse_requirements
# from pip.download import PipSession
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
# INSTALL_REQS = parse_requirements('requirements.txt', session=PipSession())
# install_requires=[str(ir.req) for ir in INSTALL_REQS]

setup(
    name='aws-decorators',
    version='0.0.2',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    description='decorators for aws things',
    long_description='decorators for aws things',
    url='https://github.com/meganlkm/aws-decorators',
    author='meganlkm',
    author_email='devstuff.io@gmail.com',
    install_requires=['boto3']
)
