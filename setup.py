from setuptools import find_packages, setup
from typing import List 

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a requirements.txt file,
    excluding editable installs indicated by '-e .' in the file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if not req.startswith('-e')]
    return requirements

setup(
    name='UAV-Based Precision Farming with Machine Learning Integration',
    version='0.0.1',
    author='Anurag',
    author_email='anuragjkl2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
