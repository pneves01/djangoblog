from django.contrib import admin
from .models import Post
'''admin.site.register(Post)'''

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    list_filter = ('created_date', 'published_date')
    ordering = ('-created_date',)