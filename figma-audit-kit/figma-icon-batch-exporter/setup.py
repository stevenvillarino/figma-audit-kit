#!/usr/bin/env python3
"""
Setup script for Figma Icon Library Batch Exporter
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="figma-icon-batch-exporter",
    version="1.0.0",
    author="Steven Villarino",
    description="A Python script for batch exporting SVG icons from Figma component libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/figma-icon-batch-exporter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Build Tools",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "figma-export=figma_icon_exporter:main",
        ],
    },
)
