from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'seller', 'phone')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': "form-control input display-7",
                    'required': "required",
                    'id': "name-form3-2w",
                    'placeholder': '이름',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': "form-control input display-7",
                    'required': "required",
                    'id': "name-form3-2w",
                    'placeholder': '성',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'type': 'email',
                    'class': "form-control input display-7",
                    'required': "required",
                    'id': "name-form3-2w",
                    'placeholder': '이메일',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': "form-control input display-7",
                    'required': "required",
                    'id': "name-form3-2w",
                    'placeholder': '전화번호',
                }
            ),
        }


