import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='aws-decorators',
    version='0.0.7',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    description='decorators for aws things',
    long_description='decorators for aws things',
    url='https://github.com/meganlkm/aws-decorators',
    author='meganlkm',
    author_email='megan.lkm@gmail.com',
    keywords=['aws', 'decorators'],
    install_requires=['boto3>=1.4.3,<=1.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities'
    ]
)
