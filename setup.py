from setuptools import setup

setup(
    name="nmapdb",
    version="1.3.0",
    description="A tool that parses xml outputs from nmap and inserts it into a SQLite database.",
    author="@haukurk",
    author_email="haukur@hauxi.is",
    packages=["nmapdb"],
    install_requires=[],
    url='https://github.com/haukurk/nmapdb',
    download_url='https://github.com/haukurk/nmapdb/releases/tag/v0.2.1',
    keywords=['nmap', 'sqlite', 'database'],
    classifiers=[],
	entry_points = {
        'console_scripts': ['nmapdb=nmapdb.__main__:default'],
    }
)