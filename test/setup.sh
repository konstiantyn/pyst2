#!/bin/sh
pip install ${TRAVIS_BUILD_DIR} coverage
cd ${TRAVIS_BUILD_DIR}
#chmod a+rw .coverage
#chown asterisk:asterisk .coverage
coverage run --rcfile=.coveragerc.asterisk test/other.py
#coverage run --source ./ -m pytest