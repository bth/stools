from setuptools import setup, find_packages

setup(
    name='stools',
    version='0.3',
    description='tools for automate tasks on machines with only ssh',
    url='https://github.com/bth/stools',
    author='bth',
    author_email='contactbth@gmail.com',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'stools = stools.main:main',
        ],
    }
)
