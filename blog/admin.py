from django.contrib import admin

# Register your models here.
from .models import BlogAuthor, Blog, BlogComment

admin.site.register(BlogAuthor)
admin.site.register(BlogComment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'post_date')