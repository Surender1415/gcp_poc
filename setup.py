"""
Package Application files
"""
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='gcp_poc',
    version="0.1",
    description='PySpark Template EGG',
    setup_requires=['wheel'],
    packages=find_packages(exclude=["*.tests"]),
    scripts=['src/main.py'],
    data_files={'config/app.ini'},
    python_requires='>=3.6',
	install_requires=requirements,
	url=https://github.com/Surender1415/gcp_poc/
    zip_safe=False
)
