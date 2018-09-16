# Python Ethereum Signing Utils

[![Build Status](https://travis-ci.org/rmeissner/py-eth-sig-utils.svg?branch=master)](https://travis-ci.org/rmeissner/py-eth-sig-utils)
[![PyPI version](https://badge.fury.io/py/py-eth-sig-utils.svg)](https://badge.fury.io/py/py-eth-sig-utils)

### Type Data Hashes

This utils contain methods to generate hashes of typed data based on [EIP-712](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-712.md).

### Setup

1. `virtualenv env -p python3`
1. `pip install -r requirements.txt`
1. `python -m unittest`

### Deploy

Library is automatically deployed if a tag is created.

Manual deployment can be peformed with:
```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```