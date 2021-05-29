from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import PasswordInput, TextInput, EmailField

User=get_user_model()




class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(label='email',widget=forms.TextInput(attrs={'placeholder': 'email','class':'contactus'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder': 'username','class':'contactus'}))
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'placeholder': 'password','class':'contactus'}))
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput(attrs={'placeholder': 'confirm password','class':'contactus'}))
    class Meta:
        model    = User
        fields = ('email','username','password1','password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        
        fields = ('email','username','first_name','last_name','date_of_birth','profile_image','background_image')



class LoginForm(forms.Form):
    
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'placeholder': 'Email Address','id':'id_email','class':'contactus',}))  
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Password','id':'id_password','class':'contactus',}))

    class Meta:
        model = User
        fields = ('email','password')
        exclude = ['username']

  
   

