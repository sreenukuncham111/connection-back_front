from django.shortcuts import render
from app.models import *
# Create your views here.
def dis_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'dis_topics.html',d)

def dis_webpages(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'dis_webpages.html',d)

def dis_access(request):
    QSA=Access.objects.all()
    d={'Records':QSA}
    return render(request,'dis_access.html',d)