#!/usr/bin/env python3

from setuptools import setup

setup(
    name = "tsautomute",
    scripts = ["tsautomute"],
    version = "1.0.0",
    install_requires = ["docopt", "pulsectl"],
    author = 'Felix "KoffeinFlummi" Wiegand',
    author_email = "koffeinflummi@protonmail.com",
    description = "Adjusts PA input volume when someone is talking",
    license = "MIT",
    keywords = "",
    url = "",
    classifiers = []
)
