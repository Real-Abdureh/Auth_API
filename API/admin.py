from django.contrib import admin

from API.models import User, Profile, Todo, ChatMessage

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verify']
    list_display = ['user', 'full_name', 'verify']

class TodoAdmin(admin.ModelAdmin):
    list_editable = ['completed']
    list_display = ['user', 'title', 'completed', 'date']

class ChatMessageAdmin(admin.ModelAdmin):
    list_editable = ['is_read']
    list_display = ['sender', 'receiver', 'message', 'is_read']



admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)    
admin.site.register(ChatMessage, ChatMessageAdmin)    
admin.site.register(Todo, TodoAdmin)    


# Register your models here.
