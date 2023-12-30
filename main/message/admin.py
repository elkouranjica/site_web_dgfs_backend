from django.contrib import admin
from main.message.models import Message
from django.contrib.auth import settings


PAGE_SIZE = settings.PAGE_SIZE


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ["mail_address", "mail_object", "created"]
	list_filter = ["mail_address"]
	list_per_page = PAGE_SIZE
	ordering = ["mail_address"]
	search_fields = ["mail_object", "mail_address"]

