from setuptools import setup, find_packages

setup(
    name="malbolge-toolkit",
    version="0.1.0",
    description="Development tools for the Malbolge programming language",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # No external dependencies for core functionality
    ],
    entry_points={
        'console_scripts': [
            'malbolge-toolkit=malbolge_toolkit:main',
        ],
    },
    python_requires='>=3.8',
)
