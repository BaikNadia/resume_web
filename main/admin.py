from django.contrib import admin
from .models import Service, Project, Request

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_from')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'created_at')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_processed')
