from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return render(request, 'homepage.html')
    return HttpResponse('homepage')


def BarGraph(request):  
    return render(request, 'BarGraph.html')


