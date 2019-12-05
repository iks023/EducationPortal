from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import Profile
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):
    YEARS = [x for x in range(1940,2020)]
    birth_date= forms.DateField(label='What is your birth date?', initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS))

    GENS = (
    ("Female", ("Female")),
    ("Male", ("Male")),
    ("Other", ("Other"))
    )

    gender = forms.ChoiceField(choices=GENS)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17)
    location = forms.CharField(required=True)
    specialty = forms.CharField(required=True)

    class Meta:
        model = Profile
        fields = ['image', 'location', 'gender', 'phone_number', 'biography', 'birth_date', 'specialty']
