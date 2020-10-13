#!/bin/sh
pip install /var/lib/asterisk/agi-bin coverage
cd /var/lib/asterisk/agi-bin/
chmod a+rw .coverage
coverage run test/other.py