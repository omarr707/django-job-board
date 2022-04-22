from django.contrib import admin

# Register your models here.

from .models import Jop ,category


admin.site.register(Jop)

admin.site.register(category)