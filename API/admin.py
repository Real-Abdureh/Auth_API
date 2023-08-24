from django.contrib import admin

from API.models import User, Profile, Todo

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verify']
    list_display = ['user', 'full_name', 'verify']

class TodoAdmin(admin.ModelAdmin):
    list_editable = ['completed']
    list_display = ['user', 'title', 'completed', 'date']


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)    
admin.site.register(Todo, TodoAdmin)    


# Register your models here.
