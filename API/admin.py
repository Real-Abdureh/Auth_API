from django.contrib import admin

from API.models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verify']
    list_display = ['user', 'full_name', 'verify']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)    


# Register your models here.
