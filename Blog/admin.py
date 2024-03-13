from django.contrib import admin
from .models import Post ,Category , Comment


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name' , 'parent']
    search_fields = ['name']

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title' , 'created_at' ,'category', 'intro']
    list_filter = ['author','created_at' , 'category']
    search_fields = ['title']
    ordering = ['created_at']

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()

class CommentModelAdmin(admin.ModelAdmin):
    list_filter = ['post' , 'created_at' , ]
    ordering = ['created_at']

admin.site.register(Post ,PostModelAdmin )
admin.site.register(Category , CategoryModelAdmin)
admin.site.register(Comment ,CommentModelAdmin )