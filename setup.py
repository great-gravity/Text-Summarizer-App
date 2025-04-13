import setuptools

with open("README.md", "w+", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Abstraction-Text-Summarization"
AUTHOR_UERS_NAME = "pravinsridhar"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "pravinsrdhr@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_UERS_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"",
    project_urls={
        "Bug Tracker": f"",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)