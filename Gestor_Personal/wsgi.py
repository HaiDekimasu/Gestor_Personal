<<<<<<< HEAD
<<<<<<< HEAD
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'Gestor_Personal.settings')

application = get_wsgi_application()
=======
# import os
# import sys

# path = os.path.expanduser('~/Gestor-p/Gestor_Personal')
# if path not in sys.path:
#     sys.path.insert(0, path)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'Gestor_Personal.settings'
# from django.core.wsgi import get_wsgi_application
# from django.contrib.staticfiles.handlers import StaticFilesHandler
# application = StaticFilesHandler(get_wsgi_application())
>>>>>>> bee32cf (	modified:   Gestor_Personal/settings.py)
=======
import os
import sys

path = os.path.expanduser('~/Gestor-p/Gestor_Personal')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Gestor_Personal.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
>>>>>>> 298dd56 (	modified:   .vscode/settings.json)
