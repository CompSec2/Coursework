#!/var/www/victim.com/.venv/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/victim.com")
sys.path.insert(1, "/var/www/victim.com/.venv/lib/python3.8/site-packages/")
sys.path.insert(2, "/var/www")
from app import app as application
