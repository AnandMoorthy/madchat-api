from django.contrib import admin

from .models import DirectMessages, Groups, GroupMembers, GroupMessages

# Register your models here.

admin.site.register(DirectMessages)
admin.site.register(Groups)
admin.site.register(GroupMembers)
admin.site.register(GroupMessages)
