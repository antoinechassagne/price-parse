from setuptools import setup, find_packages

setup(
    name='cdiscount',
    version='0.1',
    description='Return the price for a given Cdiscount\'s product reference.',
    url='https://github.com/antoinechassagne/price-parser',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    python_requires='>=3.7'
    )
