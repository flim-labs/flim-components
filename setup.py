from setuptools import setup, find_packages

setup(
    name="flim_components",
    version="0.1.3",
    author="Aurora Sirigu",
    author_email="aurora.sirigu@5bits.it",
    description="A graphical library based on PyQt6 for developing and standardize FLIM LABS applications.",
    url="https://github.com/flim-labs/flim-components",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "flim_components": ["assets/*.png", "assets/*.ico", "assets/*.gif"],
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires=">=3.9",
)
