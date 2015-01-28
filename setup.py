from distutils.core import setup

setup(
    name="nmapdb",
    version="0.2.1",
    description="A tool that parses xml outputs from nmap and inserts it into a SQLite database.",
    author="@haukurk",
    author_email="haukur@hauxi.is",
    packages=["nmapdb"],
    install_requires=["requests"],
    url='https://github.com/haukurk/nmapdb',
    download_url='https://github.com/haukurk/nmapdb/releases/tag/v0.2.1',
    keywords=['nmap', 'sqlite', 'database'],
    classifiers=[]
)