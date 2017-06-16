from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, ModuleList, AuthUser, UsageLog


# Overwritten Admin functions **************************************************************
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('full_name','username','current_waiver')
    list_filter  = ('current_waiver',)

    fieldsets = (
        ('Administrative',{'fields':('username','rfid','current_waiver',)}),
        ('Personal info',{'fields':('full_name','short_name','email','phone_number',)}),
    )

    add_fieldsets = ((None,
        {'classes':('wide',),
         'fields':('full_name','email','password1','password2')}),
    )

# Admin registrations **********************************************************************
admin.site.register(User, UserAdmin)
admin.site.register(ModuleList)
admin.site.register(AuthUser)
admin.site.register(UsageLog)
