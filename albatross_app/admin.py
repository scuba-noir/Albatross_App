from django.contrib import admin
from .models import contactFormRecords

# Register your models here.
@admin.register(contactFormRecords)
class contactFormAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','message')
