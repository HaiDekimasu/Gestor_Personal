<<<<<<< HEAD

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'Gestor_Personal.settings')
=======
import os
import sys
from django.core.wsgi import get_wsgi_application
path = os.path.expanduser('~/Gestor-p/Gestor_Personal')
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Gestor_Personal.settings'
>>>>>>> 8bfc7ca (	modified:   Gestor_Personal/wsgi.py)

application = get_wsgi_application()
