from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']

admin.site.register(UserProfile, UserProfileAdmin)


class AtricleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'promote']
    search_fields = ['title', 'content']
    
admin.site.register(Article, AtricleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']

admin.site.register(Category, CategoryAdmin)