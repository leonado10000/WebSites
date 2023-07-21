from django.shortcuts import render
from .models import *
# Create your views here.
def dummy(request):
    return None

def getData():
    data = []    
    # for i in Granger.objects.all():
    #     tgs =  []
    #     tempData = [i.P_id,i.title,i.auther,i.date,i.description,i.category,i.likes(),i.tages(),i.image.url]
    #     data.append(tempData)
    return data

def mainPage(request):
    data = getData()
    return render(request, 'App.html', {
        "data":data
    })

def addPage(request):
    return render(request, "addPage.html")