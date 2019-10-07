from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('title',)}),
        ('Advanced Options', {'classes': ('collapse',), 'fields': ('author',)}),
        ('Advanced Options2', {'classes': ('collapse',), 'fields': ('text',)})
    ]
    list_display = ('title', 'author', 'created_at')
