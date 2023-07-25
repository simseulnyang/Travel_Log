from django.contrib import admin
from .models import Post, Category, Comment, HashTag

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer', 'thumbnail']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
