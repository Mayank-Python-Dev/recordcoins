from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(UserDetail)
class UserAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Address', 'City']


admin.site.register(UserShare)
admin.site.register(UserTransaction)
admin.site.register(UserWallet)
admin.site.register(Userfollow)
admin.site.register(UserContent)
