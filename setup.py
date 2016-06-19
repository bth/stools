from setuptools import setup, find_packages

setup(
    name='stools',
    version='0.2',
    description='tools for automate tasks on machines with only ssh',
    url='https://github.com/bth/stools',
    author='bth',
    author_email='contactbth@gmail.com',
    packages=find_packages(),
    package_data={'stools': ['spec/*.configspec', 'example/*.cfg']},
    entry_points = {
        'console_scripts': [
            'stools = stools.main:main',
        ],
    }
)
