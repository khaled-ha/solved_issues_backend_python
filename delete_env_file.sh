#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'

if [ -a venv ]; then
    rm -rf venv
else
    echo -e " $RED Alert"
    echo -e 'already \033[0;31m venv \033[0;31m deleted'
fi