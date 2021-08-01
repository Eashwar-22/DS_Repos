
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()



setup(
    name='tools_',
    version='0.0.1',
    author='Easwaran T H',
    author_email='hariharaneaswaran@gmail.com',
    description='Tools for EDA and ML',
    long_description = readme(),
    long_description_content_type='text/markdown',
    classifiers =[
                    'Development Status :: 5 - Production/Stable',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 3',
                    'Operating System :: OS Independent'
                 ],


    url='https://github.com/Eashwar-22/DS_Repos/tree/eda',
    keywords = 'eda',
    license = 'MIT',

    packages='find',
    install_requires=[],
    include_package_data = True,
    zip_safe = False
)