from setuptools import setup, find_packages
from typing import List, Any


def get_requirements() -> List[str]:
    requirements_list : List[str] = []
    
    return requirements_list

setup(
    name= "Question Answer ChatBot",
     version='0.0.0.0',
    author="Nishant Borkar",
    author_email="nishantborkar139@gmail.com",
    description="Question Answer ChatBot",
    packages=find_packages(),
    install_requires=get_requirements()
)