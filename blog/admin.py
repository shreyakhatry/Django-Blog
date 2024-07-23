# from django.contrib import admin
# from .models import Post

# # Register your models here.

# admin.site.register(Post)
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If this is a new post
            obj.author = request.user
        super().save_model(request, obj, form, change)



