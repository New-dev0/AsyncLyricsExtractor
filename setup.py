import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="asynclyrics_extractor",
    version="0.0.7",
    description="Get Lyrics for any songs with speed of async Python Library.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/New-dev0/AsyncLyricsExtractor",
    author="New-dev0",
    author_email="Newdev0@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["lyrics_extractor"],
    include_package_data=True,
    install_requires=["beautifulsoup4", "aiohttp"],
    entry_points={
        "console_scripts": [
            "lyrics_extractor=lyrics_extractor.lyrics:SongLyrics",
        ]
    },
)
