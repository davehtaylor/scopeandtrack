#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/scopeandtrack/public_html/api/py")

from __init__ import app as application