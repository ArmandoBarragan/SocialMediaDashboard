from django import forms
from dashboard.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('business_name', 'email')

