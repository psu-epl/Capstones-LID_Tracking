from django import forms as f
from django.forms import ModelForm
from .models import *

# Create the view and html form templates here

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ModuleListForm(ModelFrom):
    class Meta:
        model = ModuleList
        fields = '__all__'

class AuthUserForm(ModelForm):
    class Meta:
        model = ModuleList
        fields = '__all__'

class UsageLogForm(ModelForm):
    class Meta:
        model = UsageLog
        fields = '__all__'


