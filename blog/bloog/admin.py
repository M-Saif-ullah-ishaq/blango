from django.contrib import admin
from bloog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)