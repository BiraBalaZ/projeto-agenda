from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = 'id',
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'created_date', 'description',
    search_fields = 'id', 'first_name', 'last_name', 'phone', 'email', 'created_date', 'description',
    list_filter = ('created_date'),
    list_per_page = 30
    list_max_show_all = 200
    # list_editable = 'first_name', 'last_name',
    list_display_links = 'first_name',
