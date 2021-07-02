import os
from setuptools import setup, find_packages

with open(os.path.join(os.getcwd(), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "pycobb",
    version = "0.0.4",
    author = "Ryan Byrne",
    author_email = "ryan@byrne.es",
    keywords = "baseball savant sabermetrics pycobb",
    url = "https://github.com/ryan-byrne/pycobb",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas', 'requests', 'matplotlib'
    ],
    zip_safe=False,
    entry_points = {"console_scripts": ["pycobb = pycobb.cli:main"]},
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>3.5',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 4 - Beta"
    ],
    project_urls={
        "Documentation":"https://pycobb.readthedocs.io/en/latest/",
        "Bug Reports":"https://github.com/ryan-byrne/pycobb/issues"
    },
)
