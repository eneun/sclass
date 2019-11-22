from django import forms
from .models import Class, Review

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_title', 'summary', 'describe', 'price', 'date', 'category', 'max_number', 'img1', 'img2', 'img3', 'img4', 'img5']
        widgets={
            'class_title' : forms.TextInput(
                attrs={
                    'class':'form-control input display-7',
                }
            ),

            'summary': forms.TextInput(
                attrs={
                    'class':'form-control input display-7',
                }                
            ),

            'describe' : forms.Textarea(
                attrs={
                    'class':'form-control input display-7',
                }                
            ),
            'price' : forms.TextInput(
                attrs={
                    'type' : 'number',
                    'class' : 'form-control'
                }
            ),
            'category' : forms.Select(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'max_number' : forms.TextInput(
                attrs={
                    'type' : 'number',
                    'class' : 'form-control'
                }
            ), 
            'date' : forms.TextInput(
                attrs={
                    'type' : 'date',
                    'class' : 'form-control'
                }
            ),
            'img1' : forms.FileInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'img2' : forms.FileInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'img3' : forms.FileInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'img4' : forms.FileInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
            'img5' : forms.FileInput(
                attrs={
                    'class' : 'form-control'
                }
            ),
        }

        labels={
            'class_title' : '클래스 이름',
            'summary' : '클래스 한 줄 요약',
            'describe' : '클래스 세부설명',
            'price' : '강의료',
            'date' : '날짜',
            'category' : '카테고리',
            'max_number' : '최대 수강 인원',
            'img1' : '이미지 1번',
            'img2' : '이미지 2번',
            'img3' : '이미지 3번',
            'img4' : '이미지 4번',
            'img5' : '이미지 5번',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rate', 'content')

        