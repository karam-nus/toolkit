from setuptools import setup, find_packages

setup(
    name="toolkit",
    version="0.1.0",
    packages=find_packages(include=["toolkit", "toolkit.*"]),
    install_requires=[
        # Add your package dependencies here, e.g. 'numpy>=1.18.0'
    ],
    author="Karamjot Singh",
    author_email="",
    description="Quick model evaluation and visualization tools.",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
