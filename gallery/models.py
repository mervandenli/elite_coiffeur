from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class Photo(models.Model):
    name = models.CharField(max_length=50, verbose_name='Fotoğraf Adı:')
    image = models.ImageField(upload_to='', verbose_name='Fotoğraf:')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name