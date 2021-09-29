#!/bin/bash
poetry run coverage erase && \
    poetry run mamba --enable-coverage --format=documentation specs/*_spec.py && \
	poetry run coverage html