import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Aurora-conf",
    version="0.0.2",
    author="aerocyber",
    description="A tool to share python environment by building it from scratch on target machines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aerocyber/Aurora/",
    project_urls={
        "Bug Tracker": "https://github.com/aerocyber/Aurora/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
