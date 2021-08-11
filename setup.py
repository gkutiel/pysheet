from setuptools import setup, find_packages
from version import version

with open("README.md") as f:
    long_description = f.read()

setup(
    name='pysheet',
    version=f'{version}',
    packages=find_packages(),
    long_description=long_description
    install_requires=[
        'fire',
        'numpy',
    ],
    package_data={
        'helpful_tools': ['*'],
    },
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gk-basic = basic:main',
            'gk-equation = equation:main',
            'gk-equation-xy = equation_xy:main',
        ],
    }
)
