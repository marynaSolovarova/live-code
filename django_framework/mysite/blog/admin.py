from django.contrib import admin
from .models import Post, Comment, Contact


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    search_fields = ('name', 'email', 'body')
    list_filter = ('created', 'updated')
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'message')