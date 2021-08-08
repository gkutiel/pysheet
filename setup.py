from setuptools import setup, find_packages

setup(
    name='pysheet',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'fire',
    ],
    package_data={
        'helpful_tools': ['*'],
    },
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gk-equation = equation:main',
        ],
    }
)
