from setuptools import find_packages, setup


def get_requirements() -> list[str]:

    requirements_list = []


    return requirements_list

setup(

    name = "EDA",
    version = "0.0.1",
    author = "Aditya",
    author_email = "23110016@iitgn.ac.in",
    packages = find_packages(),
    install_requires = get_requirements(),
    
)