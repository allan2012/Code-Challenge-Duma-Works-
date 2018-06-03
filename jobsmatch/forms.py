from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'}))
    
    
class AdminForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(max_length=50)
    
    
class UserForm(forms.Form):
    username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'style': 'width: 100%;', 'placeholder': 'Username',}))
    password = forms.CharField(max_length=50,  widget=forms.PasswordInput(attrs = {'style': 'width: 100%;', 'class':'form-control'}))
    first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    last_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    email = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
  

class JobForm(forms.Form):
    title = forms.CharField(widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    description = forms.CharField(widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    certificates = forms.CharField(widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    skills = forms.CharField(widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    

class CriteriaForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    certifications = forms.CharField(widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    skills = forms.CharField(widget = forms.TextInput(attrs = {'style': 'width: 100%;',}))
    

class ProfileForm(forms.Form):
    summary = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'style': 'width: 100%;', 'placeholder': 'Profile summary', 'required':'required'}))
    skills = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'style': 'width: 100%;', 'placeholder': 'Professional comptence', 'required':'required'}))
    certifications = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'style': 'width: 100%;', 'placeholder': 'Proffessional certifications', 'required':'required'}))