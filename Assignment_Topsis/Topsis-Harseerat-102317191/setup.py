from setuptools import setup, find_packages

setup(
    name="Topsis-Harseerat-102317191",
    version="1.0.0",
    author="Harseerat",
    author_email="hsidhu_be23@thapar.edu",
    description="TOPSIS command-line implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "topsis=topsis_harseerat.topsis:main"
        ]
    },
    python_requires=">=3.6",
)
