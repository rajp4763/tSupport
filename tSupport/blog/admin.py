from django.contrib import admin
from .models import *
# Register your models here.

# category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','add_date','url')
    search_fields = ('title',)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    list_filter = ('cat',)
    list_per_page = 10
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)
admin.site.register(Slider)