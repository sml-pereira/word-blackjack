"""Minimal setup script for Word Blackjack."""

from setuptools import setup, find_packages

setup(
    name="word-blackjack",
    version="1.0.0",
    description="A terminal-based multiplayer word game — like Blackjack, but with words.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Samuel",
    license="MIT",
    url="https://github.com/YOUR_USERNAME/word-blackjack",
    packages=find_packages(),
    package_data={"word_blackjack": ["data/english_words.txt"]},
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "word-blackjack=word_blackjack.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
)
