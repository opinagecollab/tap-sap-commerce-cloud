#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="tap-sap-commerce-cloud",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="SAP and Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=[
        "tap_sap_commerce_cloud.client",
        "tap_sap_commerce_cloud.record",
        "tap_sap_commerce_cloud.record.handler"
    ],
    install_requires=[
        "singer-python==5.6.1",
        "requests==2.20.0",
    ],
    entry_points="""
    [console_scripts]
    tap-sap-commerce-cloud=tap_sap_commerce_cloud:main
    """,
    packages=find_packages(),
    package_data = {
        "schemas": ["tap_sap_commerce_cloud/schemas/*.json"]
    },
    include_package_data=True,
)
