from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=200, verbose_name='Gönderen Adı:')
    email = models.EmailField(max_length=200, verbose_name='Gönderen Maili:')
    subject = models.CharField(max_length=200, verbose_name='Mesaj Konusu:')
    message = models.TextField(verbose_name='Mesaj:')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Gönderildiği Tarih:')

    def __str__(self):
        return self.name + "-" +  self.email