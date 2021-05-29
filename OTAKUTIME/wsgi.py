from static_ranges import Ranges
from dj_static import Cling, MediaCling

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OTAKUTIME.settings')

application = get_wsgi_application()

application = Ranges(Cling(MediaCling(get_wsgi_application())))