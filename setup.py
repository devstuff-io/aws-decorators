import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()
REQUIREMENTS = []
DEPENDENCY_LINKS = []

os.chdir(os.path.normpath(BASEDIR))


with open(os.path.join(BASEDIR, 'requirements.txt')) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if ("http://" in line or "https://" in line or "ssh://" in line) and "#egg=" in line:
            parts = line.split("#egg=")
            REQUIREMENTS.append(parts[-1])
            DEPENDENCY_LINKS.append(line)
        elif len(line) and line[0] != "#" and line[0] != "-":
            REQUIREMENTS.append(line)


setup(
    name='aws-decorators',
    version=VERSION,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    description='decorators for aws things',
    long_description='decorators for aws things',
    url='https://github.com/devstuff-io/aws-decorators',
    author='meganlkm',
    author_email='devstuff.io@gmail.com',
    install_requires=REQUIREMENTS,
    dependency_links=DEPENDENCY_LINKS,
    keywords=[
        'aws',
        'decorators'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: System :: Software Distribution',
        'Topic :: Utilities'
    ]
)
