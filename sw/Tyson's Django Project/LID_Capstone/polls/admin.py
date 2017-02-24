from django.contrib import admin

from .models import Question, Choice, User, Tool, Tool_User
#added user to the list to see it in the admin page?
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(Tool)
admin.site.register(Tool_User)