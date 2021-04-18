from django.contrib import admin
from .models import Post, UserProfile, Comment, Notification
from tinymce.widgets import TinyMCE

# admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinymce.js',)