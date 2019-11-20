#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-occ-products",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_occ_products"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-occ-products=tap_occ_products:main
    """,
    packages=["tap_occ_products"],
    package_data = {
        "schemas": ["tap_occ_products/schemas/*.json"]
    },
    include_package_data=True,
)
