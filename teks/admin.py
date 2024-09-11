from django.contrib import admin
from.models import data

# Register your models here.


class dataAdmin(admin.ModelAdmin):
    list_display = (id,"username","email","password","confirm_password")
    list_display_links = ("email",)
    


admin.site.register(data,dataAdmin)




