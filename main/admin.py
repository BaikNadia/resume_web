from django.contrib import admin
from .models import Service, Project, Request

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_from')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'order')
    list_filter = ('category',)
    list_editable = ('order',)
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'category', 'description', 'preview_image', 'order')
        }),
        ('Для сайтов', {
            'fields': ('site_url',),
            'classes': ('collapse',),
        }),
        ('Для видео/анимаций', {
            'fields': ('video_url', 'video_file'),
            'classes': ('collapse',),
        }),
    )

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_processed')
