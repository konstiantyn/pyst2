#!/bin/sh
pip install ${TRAVIS_BUILD_DIR} coverage
cd ${TRAVIS_BUILD_DIR}
coverage run --rcfile=.coveragerc.asterisk test/other.py