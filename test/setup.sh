#!/bin/sh
pip install /var/lib/asterisk/agi-bin coverage
cd /var/lib/asterisk/agi-bin/
chmod a+rw .coverage
chown asterisk:asterisk .coverage
coverage run test/other.py