#!/bin/sh
pip install /var/lib/asterisk/agi-bin coverage
cd /var/lib/asterisk/agi-bin
coverage run test/other.py