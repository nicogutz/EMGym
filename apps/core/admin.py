from django.contrib import admin

from apps.core.models import *

admin.site.register([Device, Exercise, Datum])

