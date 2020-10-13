#!/bin/sh
pip install /var/lib/asterisk/agi-bin coverage
cd /var/lib/asterisk/agi-bin/
chmod a+rw .coverage
chown travis:travis .coverage
coverage run test/other.py