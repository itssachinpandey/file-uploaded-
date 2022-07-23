from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("<b>Welcome to sachin</b>")

def coures(request):
    return HttpResponse("Welcome to sachin pandey")
def homepage(request):
    data={
        'title':'HOME PAGE python',
        'bdata':'welcome to python',
        'clist':['php','java','python'],
        'cont':'contacts page',
        'number':[10,20,30,40,50,60,70,80,90],
        'stuent':[
            {'name':'abc','phone':123456789},
            {'name':'testing','phone':98764321}
        ]
    }
    return render(request,"html.html",data)

def contact(request):
    return render(request,"templates\contact.html")
