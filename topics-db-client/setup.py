from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='db_utils',
    version='0.1.7',
    packages=find_packages(),
    description='A package which include all the utils regarding the db',
    author='Amit Rechavia',
    author_email='amit.rechavia@intel.com',
    url='https://github.com/MaorEl/topics-insights',
    install_requires=required,
)
