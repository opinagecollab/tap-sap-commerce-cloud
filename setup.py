#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-sap-commerce-cloud",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_sap_commerce_cloud"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-sap-commerce-cloud=tap_sap_commerce_cloud:main
    """,
    packages=["tap_sap_commerce_cloud"],
    package_data = {
        "schemas": ["tap_sap_commerce_cloud/schemas/*.json"]
    },
    include_package_data=True
)
