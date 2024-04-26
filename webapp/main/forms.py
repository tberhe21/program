from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patients, PatientMedications, PatientCondition
# from .models import Post

# To register a user
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
# you can add firstname ...
# lastname whatever you want

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# the models below are form models connected to the ones above
    # that allows to generate a form and any changes will be linked to the models above

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'


class ConditionForm(forms.ModelForm):
    class Meta:
        model = PatientCondition
        fields = '__all__'


class MedicationForm(forms.ModelForm):
    class Meta:
        model = PatientMedications
        fields = '__all__'
