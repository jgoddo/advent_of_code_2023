import setuptools

install_deps = [
    'requests',
    'beautifulsoup4',
    'html5lib'
]

setuptools.setup(
    name="aoc_helpers",
    version="0.0.1",
    author="Example Author",
    author_email="#",
    description="aoc_helpers helper",
    url="#t",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_deps,
    package_dir={"": "src"},
    packages=['aoc_helpers'],
    python_requires=">=3.6",
)
