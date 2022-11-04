#!/bin/bash
#
# Check lint rules on the Python code.
# This code assumes that the caller has installed the testing requirements
# in test_requirements.txt.
#
# Read more here: https://github.com/Tradias-GmbH/tradias.orders
# Proprietary and confidential. Copyright Tradias-GmbH 2021

set -o xtrace
mypy  --ignore-missing-imports --disallow-untyped-defs data_service/*.py tests/*.py
# black data_service tests
pre-commit install
# pre-commit run --all-files
git ls-files -- '*.py' | xargs pre-commit run --files
exit_code="$?"
if [ $exit_code -ne 0 ]
then
exit $exit_code
fi
pylint --rcfile=pylintrc --fail-under=9.5 data_service tests
