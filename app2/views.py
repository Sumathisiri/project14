from django.shortcuts import render

# Create your views here.

def siri(request):
    return render(request,'siri.html')


def srujju(request):
    return render(request,'srujju.html')
