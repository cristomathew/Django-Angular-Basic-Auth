from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.utils.translation import gettext as _

from Core import models

class UserAdmin(BaseUser):
    ordering = ['id']
    list_display = ['id','email','username','name']
    list_display_links = ['id','email']
    fieldsets = (
        (None,{'fields':('username','email','password')}),
        (_('Personal Info'),{'fields': ('name',)}),
        (_('Permissions'),{'fields':('is_active','is_staff','is_superuser')}),
        (_('Imp dates'),{'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('username','email','password1','password2')
        }),
    )

admin.site.register(models.User,UserAdmin)