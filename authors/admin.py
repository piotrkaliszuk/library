from django.contrib import admin
from .models import AuthorModel

# Register your models here.
@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    pass