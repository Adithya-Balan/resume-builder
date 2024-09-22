from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import userinfo, education, working_info, skill, others

class RegisterForm(UserCreationForm):
    model = User
    fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class UserInfoForm(forms.ModelForm):
    
    class Meta:
        model = userinfo
        fields = ["first_name", "sur_name", "email", "city", "country", "pincode", "phone", "career_objective"]
        labels = {
            'sur_name': 'surname',
        }
        widgets = {
        'first_name' : forms.TextInput(attrs={'placeholder': 'e.g. Aravind'}),
        'sur_name' : forms.TextInput(attrs={'placeholder': 'e.g. Singh', 'label': 'surname'}),
        'email': forms.TextInput(attrs={'placeholder': 'e.g. aravindsingh@sample.in'}),
        'city': forms.TextInput(attrs={'placeholder': 'e.g. New Delhi'}),
        'country': forms.TextInput(attrs={'placeholder': 'e.g. India'}),
        'pincode': forms.TextInput(attrs={'placeholder': 'e.g. 112403'}),
        'phone': forms.TextInput(attrs={'placeholder': 'e.g. +91 9846528501'}),
        'career_objective': forms.Textarea(attrs={'placeholder': 'In 250 characters', 'rows': 5})
    }

class EducationForm(forms.ModelForm):
    
    class Meta:
        model = education
        exclude = ['user']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'school_name': forms.TextInput(attrs={'placeholder': 'e.g. Oxford'}),
            'school_location': forms.TextInput(attrs={'placeholder': 'e.g. New Delhi'}),
            'CGPA': forms.TextInput(attrs={'placeholder': '8.9'}),
            'field_of_study': forms.TextInput(attrs={'placeholder': 'Computer Science'})   
        }
        
class WorkingInfoForm(forms.ModelForm):
    
    class Meta:
        model = working_info
        exclude = ['user']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'e.g. Infosys'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Bangalore'}),
            'your_role': forms.TextInput(attrs={'placeholder': 'e.g. Full Stack Developer'}),
            'role_description': forms.Textarea(attrs={'placeholder': 'e.g. Explain your roles in few lines..', 'rows': 5})
        }
        
class SkillForm(forms.ModelForm):
    
    class Meta:
        model = skill
        fields = ['language', 'technologies', 'core']
        widgets = {
            'language': forms.CheckboxSelectMultiple, # This should work with MultiSelectField
            'technologies': forms.CheckboxSelectMultiple, 
            'core': forms.CheckboxSelectMultiple,
        }
        
class OtherForm(forms.ModelForm):
    
    class Meta:
        model = others
        exclude = ['user']
        widgets = {
            'portfolio': forms.TextInput(attrs={'placeholder': 'Your Portfolio URL'}),
            'linked_in': forms.TextInput(attrs={'placeholder': 'Your Linkedin URL'}),
            'github': forms.TextInput(attrs={'placeholder': 'Your Github URL'}),
            'leet_code': forms.TextInput(attrs={'placeholder': 'Your Leetcode URL'}),
            'other_link': forms.TextInput(attrs={'placeholder': 'e.g. Other Attachment'}),
            'projects': forms.Textarea(attrs={'placeholder': 'Share all the projects you have worked on', 'rows': 5})
        }
        