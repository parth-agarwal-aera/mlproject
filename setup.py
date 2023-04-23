from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This finction will return the list of requirements
    '''
    with open(file_path,'r') as file_obj:
        req = file_obj.readlines()
        req = [x.replace('\n','') for x in req]
        req.remove('-e .')
    
    return req



setup(
    name = 'MLPROJECT',
    version = '0.0.1',
    author = 'Parth',
    author_email = 'parth.agarwal@aeratechnology.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)
