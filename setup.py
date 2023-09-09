from setuptools import setup, find_packages

setup(
    name='movies_analyzer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Veselin Hubavenov',
    author_email='vhubavenov@gmail.com',
    description='Movies Dataset Analyzer',
    url='https://github.com/vesso8/Movies-Dataset-Analyzer.git',
)