from django.contrib import admin
from .models import data
# Register your models here.



class dataAdmin(admin.ModelAdmin):
    list_display = (id,"title","author","date","is_published","description","video")
    list_display_links = ("title",)
    


admin.site.register(data,dataAdmin)
