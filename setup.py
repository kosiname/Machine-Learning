from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT ='-e .'

def get_requirements(file_path:str) -> List[str]:
    ## THIS FUNCTION WOULD RETURN A LIST OF REQUIREMENTS
    requirements = []
    with open(file_path) as pth:
        requirements = pth.readlines()
        requirements = [req.replace("/n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name= 'Machine-Learning',
    version= '0.0.1',
    author= 'Kosiname',
    author_email= 'oduahikechukwu1@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('/Users/mac/Documents/project/MachineLearning/Machine-Learning/requirement.txt')
)