from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from . models import Candidate
from django.forms import ModelForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'
    # format='%Y/%m/%d'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    # format = ''''
class ScheduleForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
       
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'candidate_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'candidate_mail': forms.TextInput(attrs={'class': 'form-control'}),
            'candidate_cv': forms.FileInput(attrs={'class': 'form-control'}),
            'avialable_for': forms.Select(attrs={'class': 'form-select'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
            'technology': forms.Select(attrs={'class': 'form-select'}),
            'post': forms.Select(attrs={'class': 'form-select'}),
            'scheduled_date': DateInput(),
            'scheduled_time': TimeInput(),
            'scheduled_by': forms.TextInput(attrs={'class': 'form-control'}),
            'interviewr_name': forms.TextInput(attrs={'class': 'form-control'}),
            'interviewr_mail': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
        }
class UpdateStatus(ModelForm):
     class Meta:
        model = Candidate
        fields = ['status','remark']