from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Sumit Patil',
    author_email='sumitpatil141005@gmail.com',
    description='A small example package',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)