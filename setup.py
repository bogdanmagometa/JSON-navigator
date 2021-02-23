import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JSON-navigator", # Replace with your own username
    version="0.0.1",
    author="Bohdan Mahometa",
    author_email="bohdan.mahometa@ucu.edu.com",
    description="A project for navigating JSON file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bogdanmagometa/JSON-navigator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
