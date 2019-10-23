from setuptools import setup, find_packages

packages = find_packages(
        where='.',
        include=['src*', 'logs*']
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='logger',
    version='0.1',
    description='logger library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cm107/logger",
    author='Clayton Mork',
    author_email='mork.clayton3@gmail.com',
    license='MIT License',
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pylint>=2.4.2'
    ],
    python_requires='>=3.6'
)