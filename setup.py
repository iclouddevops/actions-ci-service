from setuptools import setup, find_packages


with open("requirements.txt", encoding="utf-8") as f:
    next(f)
    requirements = f.read().strip().split("\n")



setup(
    name='sdk',
    version='0.1',
    description='My Python SDK for a specific service',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(where="my_sdk"),
    install_requires=requirements,
)