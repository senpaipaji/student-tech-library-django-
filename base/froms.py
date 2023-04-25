from django.forms import ModelForm, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Subject, Comment


class SubjectForm(ModelForm):

    class Meta:
        required = True
        model = Subject
        fields = ['branch', 'semester']
        widgets = {
            'branch': Select(attrs={
                'class': "form-input",
                'name': "branch"
            }),
            'semester': Select(attrs={
                'class': "form-input",
                'name': "semester"
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'message']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']