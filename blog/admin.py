from django.contrib import admin
from .models import Articles

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Articles, ArticleAdmin)