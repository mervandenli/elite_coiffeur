from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.contrib import messages
from .forms import FeedbackForm


# Create your views here.

def switch_lang(request):
    return render(request, 'pages/index.html')
def index(request):
    return render(request, 'pages/index.html')
def about(request):
    return render(request, 'pages/about.html')
def price(request):
    return render(request, 'pages/price.html')
def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid(): #başarılı ise
            form.save()
            messages.success(request, "Message sent.")
            return redirect('contact')
    else: # başarısız ise
        form = FeedbackForm()
    return render(request, 'pages/contact.html', {'form': form})