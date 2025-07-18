
'''
The setup.py file is responsible for packaging and distributing 
python project
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path)->List[str]:
    """This function will return list of requirements"""

    requirement_list = []
    try:
        with open(file_path,'r') as file:
            ##Read Lines from the file
            lines = file.readlines()
            ##Process each line
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e.
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
        return requirement_list
    except FileNotFoundError:
        print("requirements.txt not found")

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="prudhvi ganesh",
    author_email="prudhviredrouth143@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)


