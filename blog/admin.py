from django.contrib import admin
from .models import Post, Comment, HashTag

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
