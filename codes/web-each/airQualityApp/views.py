from django.shortcuts import render
import os 
from .forms import EmailListForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def mission(request):
    return render(request, 'mission.html')

def gallery(request):
    gallery_path = os.path.join('static', 'gallery')
    gallery_files = os.listdir(gallery_path)
    gallery_urls = [os.path.join(gallery_path, url) for url in gallery_files]
    print(gallery_urls)

    context = {"gallery_urls": gallery_urls}
    return render(request, 'gallery.html', context)

def air(request):
    api_key = '150D1602-6B37-4735-9D6E-A659F17576CF'
    context = {'api_key': api_key}
    return render(request, 'air.html', context)

def email(request):
    if request.method == 'POST':
        form = EmailListForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmailListForm()
    
    return render(request, 'email.html', {'form': form})
