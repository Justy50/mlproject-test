from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will dynamically get the package list from requirement.txt
    
    '''

    requirement = []

    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('/n', "") for req in requirement]

    return requirement


setup(
name = 'mlproject',
version = '1.0.0',
author = "Justine Miranda",
author_email = "mjustine726@gmail.com",
packages = find_packages(),
install_requires = get_requirements('requirement.txt')
)