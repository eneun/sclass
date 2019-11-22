from django.shortcuts import render, get_object_or_404
from cardnews.models import News

# Create your views here.
def news_list(request):
    news = News.objects
    return render(request, 'cardnews/news_list.html', {'news':news})

def news_content(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'cardnews/news_content.html', {'news':news})