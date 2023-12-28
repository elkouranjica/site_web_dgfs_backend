from django.contrib import admin
from main.institution.models import Ministere, Direction, Service, Directeur, ChefService


admin.site.register(Ministere)

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
	list_display = ['name', 'direction_generale', 'ministere']
	list_filter = ['direction_generale']


admin.site.register(Service)
admin.site.register(Directeur)
admin.site.register(ChefService)
