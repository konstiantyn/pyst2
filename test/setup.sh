#!/bin/sh
pip install /home/travis/build/invitecomm/pyst2 coverage coveralls pytest
cd /home/travis/build/invitecomm/pyst2
#chmod a+rw .coverage
#chown asterisk:asterisk .coverage
coverage run --rcfile=.coveragerc.asterisk test/other.py
#coverage run --source ./ -m pytest