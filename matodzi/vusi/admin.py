from django.contrib import admin
from .models import Contact

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')

admin.site.register(Contact, ContactMessageAdmin)

