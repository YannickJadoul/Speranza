from setuptools import setup, Extension

setup(
    name="spam",
    ext_modules=[Extension('spam', sources=['spam.cpp'], language="c++")],
    version="0.1.0",
)
