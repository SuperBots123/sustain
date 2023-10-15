from django import forms
from users.models import Sustainer  # Replace with your actual model

class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = Sustainer
        fields = ['about', 'city', 'state', 'linked_in', 'profile_picture']
