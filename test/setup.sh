#!/bin/sh
pip install /var/lib/asterisk/agi-bin coverage coveralls pytest
cd /var/lib/asterisk/agi-bin/
#chmod a+rw .coverage
#chown asterisk:asterisk .coverage
#coverage run --source ./ test/other.py
coverage run --source ./ -m pytest