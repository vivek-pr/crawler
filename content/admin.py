from django.contrib import admin
from .models import Content, Tags, Source, Media
# Register your models here.

admin.site.register(Content)
admin.site.register(Tags)
admin.site.register(Source)
admin.site.register(Media)


