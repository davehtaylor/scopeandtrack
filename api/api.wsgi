import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append("/var/www/scopeandtrack/public_html/api")

from api import app as application