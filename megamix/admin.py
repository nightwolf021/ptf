from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.member)
admin.site.register(models.programming_language)
admin.site.register(models.project)
admin.site.register(models.customer_message)
