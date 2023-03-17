from django.shortcuts import render

# Create your views here. 

def dhoni(request):
    return render(request,'dhoni.html')

def suresh(request):
    return render(request,'suresh.html')
