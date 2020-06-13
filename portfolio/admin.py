from django.contrib import admin
from .models import *

# Register your models here.

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'email', 'subject','date',)
    search_fields = ('first_name','last_name', 'email',)
    date_hierarchy = 'date'

admin.site.register(Contactus, ContactusAdmin)

admin.site.register(Work)
admin.site.register(Dcoder)
admin.site.register(Aboutme)
admin.site.register(Prog)
admin.site.register(Gallery)
admin.site.register(Myimgacceuil)