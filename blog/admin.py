from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','published_date')
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
  