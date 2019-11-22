from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import User
from classregister.models import Class, Scrap, Review, Book
from storeregister.models import Store, Recommend
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
# Create your views here.

def signup(request):
    #signup 버튼을 눌렀을 때 일어나야 하는 일
    if request.method == 'POST': #form으로 넘긴 값이 POST 이면
        if request.POST['password1'] == request.POST['password2']:  #비밀번호 두 개가 서로 일치하면
            try:
                user = User.objects.get(username=request.POST['username']) #POST 형식으로 가져온 username 과 일치하는 User 객체의 username을 가져와서 user 변수에 저장
                return render(request, 'accounts/signup.html', {'error':'이미 존재하는 아이디입니다'})
            except User.DoesNotExist:    #username과 일치하는 값을 가진 객체가 없어서 try 를 실행하지 못한 경우
                user = User.objects.create_user(    #User객체 새로 생성 POST로 가져온 username과 password1 필드에 저장
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)         #로그인 실행
                return redirect('profile_edit')
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다'})
    else: 
        return render(request, 'accounts/signup.html') 


def login(request):
    if request.method == 'POST':    #로그인 버튼을 눌렀을때 
        username = request.POST['username']    #username 저장
        password = request.POST['password']    #password 저장
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:    #사용자가 정보를 알맞게 입력한 경우
            auth.login(request, user)   #로그인 실행
            return redirect('home')     #홈으로 이동
        else:
            return render(request, 'accounts/login.html', {'error': '아이디나 비밀번호가 일치하지 않습니다'})
    else: 
        return render(request, 'accounts/login.html')

def signup_complete(request):
    return render(request, 'accounts/signup_complete.html') 

@login_required   
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')

@login_required
def mypage(request):
        user = User.objects.get(username=request.user)
        return render(request, 'accounts/mypage.html', {'user':user})

@login_required
def my_class(request):
    classes = Class.objects.filter(owner_name=request.user)
    return render(request, 'accounts/my_class.html', {'classes' : classes})

def my_consult(request):
    return render(request, 'accounts/my_consult.html')

@login_required
def my_recommend(request):
    recommends = Recommend.objects.filter(user=request.user)
    return render(request, 'accounts/my_recommend.html', {'recommends': recommends})

@login_required
def my_review(request):
    reviews = Review.objects.filter(user=request.user)
    return render(request, 'accounts/my_review.html', {'reviews': reviews})

@login_required    
def my_scrap(request):
    scraps = Scrap.objects.filter(user=request.user)
    return render(request, 'accounts/my_scrap.html', {'scraps':scraps})

@login_required
def my_store(request):
    stores = Store.objects.filter(user = request.user)
    return render(request, 'accounts/my_store.html', {'stores':stores}) 

@login_required
def my_student(request, class_id):
    myclass = get_object_or_404(Class, pk = class_id)
    books = Book.objects.filter(book_class=myclass)
    current_number = myclass.book_set.count()
    return render(request, 'accounts/my_student.html', {'class':myclass, 'books':books, 'current_number':current_number}) 

@login_required
def my_enroll(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'accounts/my_enroll.html', {'books': books}) 

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            print("valid")
            user_form.save()
            return redirect('profile_show')
            # messages.success(request, ('Your profile was successfully updated!'))
        else:
            print("invalid")
            return redirect('profile_show')
            # messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        return render(request, 'accounts/profile_edit.html', {'user_form':user_form})
    return render(request, 'accounts/profile_edit.html') 

@login_required
def profile_show(request):
    return render(request, 'accounts/profile_show.html') 

###데코레이션
#로그인, 사인업 안돼있으면 