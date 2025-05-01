from django.contrib import admin
from .models import Category, Location, Post

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)


# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'author', 'category', 'pub_date', 'is_published')
#     search_fields = ('title', 'author__username', 'category__name')
#     list_filter = ('category', 'is_published', 'pub_date')
