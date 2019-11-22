from django.db import models

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=100)
    photo1 = models.ImageField(null=True, blank=True, upload_to='news/')
    photo2 = models.ImageField(null=True, blank=True, upload_to='news/')
    photo3 = models.ImageField(null=True, blank=True, upload_to='news/')
    photo4 = models.ImageField(null=True, blank=True, upload_to='news/')
    photo5 = models.ImageField(null=True, blank=True, upload_to='news/')
    photo6 = models.ImageField(null=True, blank=True, upload_to='news/')
    photo7 = models.ImageField(null=True, blank=True, upload_to='news/')
    photo8 = models.ImageField(null=True, blank=True, upload_to='news/')

    def __str__(self):
      return self.news_title