from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Packages)
admin.site.register(SubPackage)
admin.site.register(Destination)