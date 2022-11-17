from django.contrib import admin

# Register your models here.

from . models import post, kategori

admin.site.register(post)
admin.site.register(kategori)
