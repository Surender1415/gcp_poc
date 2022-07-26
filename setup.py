"""
Package Application files
"""
from setuptools import setup, find_packages

setup(
    name='gcp_poc',
    version="0.1",
    description='PySpark Template EGG',
    setup_requires=['wheel'],
    packages=find_packages(exclude=["*.tests"]),
    scripts=['src/main.py'],
    data_files={'config/app.ini'},
    python_requires='>=3.6',
    zip_safe=False
)
