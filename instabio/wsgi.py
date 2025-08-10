# instabio/wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instabio.settings')

# Run build commands
call_command('migrate')
call_command('collectstatic', '--noinput')

# This is the main application Vercel will use
application = get_wsgi_application()

# Vercel looks for an 'app' variable
app = application