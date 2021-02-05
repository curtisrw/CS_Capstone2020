import sys

sys.path.insert(0, "/var/www/cgi-bin/flask/public")
from cs499capstone.public.app import create_app

application = create_app()
