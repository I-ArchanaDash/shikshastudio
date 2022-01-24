from django.contrib import admin
from shikshapp.models import worklist,shikshapp_teachers
# Register your models here.
admin.site.register((shikshapp_teachers))
admin.site.register((worklist))