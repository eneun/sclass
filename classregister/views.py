from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
# 필요기능
import datetime
# 모델
from .models import Class, Book, Review, Scrap
from storeregister.models import Store
from django.conf import settings
# 폼
from .forms import ClassForm, ReviewForm

# Create your views here.
def home(request):
    return render(request, 'classregister/home.html')

def class_list(request):
    classes = Class.objects.filter(date__gte=datetime.datetime.now()).order_by('-id')
    data = { 'classes' : classes }
    return render(request, 'classregister/class_list.html', data)

def detail(request, class_id):
    class_object = get_object_or_404(Class, pk=class_id)
    books = Book.objects.filter(book_class=class_id)
    books = [ i.user for i in books ]

    user = class_object.owner_name
    store = Store.objects.filter(user=user)
    address = store.first().address

    reviews = Review.objects.filter(review_class=class_id)
    booked = Book.objects.filter(book_class=class_id, user=request.user)
    scraped = Scrap.objects.filter(user=request.user, my_class=class_object)
    data = { 'object' : class_object, 'reviews' : reviews, 'books':books, 'scraped':scraped, 'booked': booked, 'address': address}
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.review_class = class_object
            review.user = request.user
            review.save()
            return render(request, 'classregister/class_detail.html', data)
    else:
        form = ReviewForm()
        data['form'] = form
        return render(request, 'classregister/class_detail.html', data)

def register(request):
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():
            one_class = form.save(commit=False)
            one_class.owner_name = request.user
            one_class.save()
            return redirect('home')
    else:
        form = ClassForm()
        data = {'form' : form}
        return render(request, 'classregister/class_register.html', data)

def classupdate(request, class_id):
    one_class = get_object_or_404(Class, pk = class_id)
    if request.method == 'POST':
        form = ClassForm(request.POST, request.FILES, instance = one_class)
        if form.is_valid():
            one_class = form.save(commit=False)
            one_class.save()
            return redirect('classregister:detail', class_id = one_class.pk)
    else:
        form = ClassForm(instance=one_class)
        data = {'form':form}
        return render(request, 'classregister/class_edit.html', data)

def delete(request, class_id):
    one_class = get_object_or_404(Class, pk = class_id)
    if request.user != one_class.owner_name:
        return HttpResponse('글쓴이만 삭제 가능 합니다.')
    one_class.delete()
    return redirect('list')

def search(request):
    # qs = Class.objects.all()
    # q = request.GET.get('q','')
    
    # if q:
    #     qs = qs.filter(class_title__icontains=q)

    # data = { 
    #     'classes' : qs,
    #     'q' : q
    #      }
    # return render(request, 'classregister/class_list.html', data)

    category = request.GET['category']
    if category:
        if category=='none':
            classes = Class.objects.filter(date__gte=datetime.datetime.now()).order_by('-id')
        else:
            classes = Class.objects.filter(category=category) & Class.objects.filter(date__gte=datetime.datetime.now()).order_by('-id')
    data = {
        'classes': classes
    }
    
    return render(request, 'classregister/class_list.html', data)

def participate(request, class_id):
    user = get_object_or_404(get_user_model(), pk=request.user.id)
    one_class = get_object_or_404(Class, pk=class_id)
    booked = Book.objects.filter(user=user, book_class=one_class)
    if not booked:
        if one_class.book_set.count() >= one_class.max_number:
            messages.add_message(request, messages.INFO, '인원이 가득 찼습니다.')
            return redirect('classregister:detail', class_id = class_id)
        book = Book.objects.create(user=request.user, book_class=one_class)
        return redirect('classregister:detail', class_id = class_id)
    else:
        booked.delete()
        return redirect('classregister:detail', class_id = class_id)    


def scrap(request, class_id):
    user = get_object_or_404(get_user_model(), pk=request.user.id)
    one_class = get_object_or_404(Class, pk=class_id)
    scraped = Scrap.objects.filter(user=user, my_class=one_class)
    if not scraped:
        scrap = Scrap.objects.create(user=request.user, my_class=one_class)
        return redirect('classregister:detail', class_id = class_id)
    else:
        scraped.delete()
        return redirect('classregister:detail', class_id = class_id)

def recommend(request, class_id):
    return render(request, 'classregister/class_detail.html', data)

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.user:
        return HttpResponse('해당 리뷰를 쓴 유저가 아닙니다')
    review.delete()
    return redirect('classregister:detail', class_id=review.review_class.id)

def review(request, class_id):
    return render(request, 'classregister/class_detail.html', data)
