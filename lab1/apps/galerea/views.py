from django.http import Http404,HttpResponse
from django.shortcuts import render
from .models import Image

def index(request):
    latest_image = Image.objects.order_by('-image_like')[:5]
    return render(request, 'galerea/galereaList.html', {'latest_image' : latest_image})

def top(request):
    top_image = Image.objects.order_by('-image_like')
    return render(request, 'galerea/galereaTop.html', {'top_image' : top_image})


def like(request, image_id):
    try:
        a = Image.objects.get(id = image_id)
    except:
        raise Http404("not found")

    a.image_like += 1 
    a.save()

    latest_image = Image.objects.order_by('-image_like')[:5]
    return render(request, 'galerea/galereaList.html', {'latest_image' : latest_image})

def dislike(request, image_id):
    try:
        a = Image.objects.get(id = image_id)
    except:
        raise Http404("not found")

    a.image_like -= 1 
    a.save()

    latest_image = Image.objects.order_by('-image_like')[:5]
    return render(request, 'galerea/galereaList.html', {'latest_image' : latest_image})