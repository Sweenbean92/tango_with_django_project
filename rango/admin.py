from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ('title', 'category', 'url')

class CategotyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategotyAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)