from django.contrib import admin

# Register your models here.
from .models import dl
# what ever class we made in models.py we have to import here by class name…
admin.site.register(dl) #

from .models import registration
admin.site.register(registration)
