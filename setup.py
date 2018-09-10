import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_eth_sig_utils",
    version="0.1.0",
    author="Richard Meissner",
    author_email="msc.meissner@gmail.com",
    description="Python Ethereum Signing Utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rmeissner/py-eth-sig-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)