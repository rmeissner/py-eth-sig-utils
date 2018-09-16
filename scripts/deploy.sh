#!/bin/bash
# fail if any commands fails
set -e

python -m pip install --upgrade setuptools wheel
python -m pip install --upgrade twine

python setup.py sdist bdist_wheel
twine upload -u $PYPI_USER -p $PYPI_PASS dist/*