from django.contrib import admin
from .models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "active"]
    search_fields = ["title", "slug", "author"]
    prepopulated_fields = {'slug': ("title",)}

admin.site.register(BlogPost, BlogPostAdmin)