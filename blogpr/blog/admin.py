from django.contrib import admin
from .models import Post

class PostModel(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created']
    search_fields = ['title', 'author']
    
# Register your models here.
admin.site.register(Post, PostModel)
