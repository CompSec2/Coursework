#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
from app import app as application
sys.path.insert(0, "/var/www/victim.com")
