from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='servercontrol',
    version='0.0.1',
    author="Albert Quiroga",
    author_email="albertquirogabertolin@gmail.com",
    description="Small Python CLI utilities to manage HP iLO servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertquiroga/servercontrol",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'server=servercontrol.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Utilities"
    ],
    install_requires=['albertquiroga_utils', 'paramiko'],
    python_requires='>=3.0'
)
