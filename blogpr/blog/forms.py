#Manage forms
from django import forms
from .models import Post

#class based
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'date_created']

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        label='Username'
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        label='Password'
        )
        