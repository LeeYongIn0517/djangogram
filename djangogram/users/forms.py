from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.db.models import fields
from django.utils.translation import gettext_lazy as _
from django import forms as django_forms

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }
class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User #????
        fields = ['email', 'name', 'username', 'password']