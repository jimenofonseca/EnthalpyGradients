from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ['numpy',
                    'pandas']

setup(
    name='EnthalpyGradients',
    version='1.0',
    packages=['EnthalpyGradients'],
    url='https://github.com/JIMENOFONSECA/EnthalpyGradients',
    license='MIT',
    author='Jimeno A. Fonseca',
    author_email='fonseca.jimeno@gmail.com',
    description='Library for calculation of daily enthalpy gradients',
    long_description=long_description,
    python_requires='>=3.6',
    install_requires=install_requires,
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"]
)