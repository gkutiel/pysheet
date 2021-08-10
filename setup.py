from setuptools import setup, find_packages

setup(
    name='pysheet',
    version='0.0.1',
    packages=find_packages(),
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
        ],
    }
)
