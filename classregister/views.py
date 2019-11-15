from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Class

from .forms import ClassForm

# Create your views here.
def home(request):
    return render(request, 'classregister/home.html')

def class_list(request):
    classes = Class.objects.all().order_by('-id')
    data = { 'classes' : classes }
    return render(request, 'classregister/class_list.html', data)

def detail(request, class_id):
    class_object = get_object_or_404(Class, pk=class_id)
    data = { 'object' : class_object }
    return render(request, 'classregister/class_detail.html', data)

def register(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            one_class = form.save(commit=False)

            # user가 신청하는 곳에 갈 것
            # try:
            #     if one_class.current_number == one_class.max_number:
            #         raise ValueError
            # except ValueError:
            #     return HttpResponse("인원이 가득찼습니다!")

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
        form = ClassForm(request.POST, instance = one_class)
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
    one_class.delete()
    return redirect('list')

def search(request):
    qs = Class.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(class_title__icontains=q)

    data = { 
        'classes' : qs,
        'q' : q
         }
    return render(request, 'classregister/class_list.html', data)

def scrap(request, class_id):
    return render(request, 'classregister/class_detail.html', data)

def recommend(request, class_id):
    return render(request, 'classregister/class_detail.html', data)

def review(request, class_id):
    return render(request, 'classregister/class_detail.html', data)