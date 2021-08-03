from django.shortcuts import render
from django.utils.translation import ugettext as _
from .models import Photo

# Create your views here.
def gallery(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos
    }

    return render(request, 'pages/gallery.html', context)
