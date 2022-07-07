"""
WSGI config for easycare project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys
sys.path.append('/var/www/Easyproject/easycare')
sys.path.append('/var/www/Easyproject/venv/lib/python3.6/site-packages')
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easycare.settings')

try:
    application = get_wsgi_application()
except Exception:
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(),signal.SIGINT)
        time.sleep(2.5)
