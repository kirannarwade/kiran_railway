from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import ContactUs


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        lables = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})}

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email  

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("An user with this username already exists!")
        return username  
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'mobile_number', 'hobbies', 'messege']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
                    'mobile_number':forms.NumberInput(attrs={'class':'form-control'}),
                    'hobbies':forms.Select(attrs={'class':'form-control'}),
                    'messege':forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
                    }
