from setuptools import setup, find_packages

setup(
    name="flim_components",
    version="0.1.0",
    author="Aurora Sirigu",
    author_email="aurora.sirigu@5bits.it",
    description="A graphical library based on PyQt6 for developing and standardize FLIM LABS applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/flim-labs/flim-components",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: User Interfaces",
        "Framework :: PyQt",
    ],
    python_requires=">=3.9",
    install_requires=[
        "PyQt6>=6.7.0",
        "PyQt6-Qt6>=6.7.0",
        "PyQt6-sip>=13.6.0",
        "pyqtgraph>=0.13.4",
        "numpy>=1.26.4",
        "matplotlib",
    ],
)
