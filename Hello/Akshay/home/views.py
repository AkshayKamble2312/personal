from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    templates = 'index.html'
    return render(request,templates)
    # return HttpResponse("this is home page")

def about(request):
    templates = 'about.html'
    return render(request,templates)
    # return HttpResponse("this is about page")

def services(request):
    tempates = 'services.html'
    return render(request,tempates)
    # return HttpResponse("this is services page")    

    
def getcontact(request):
    if request.method =="POST":
        firstname= request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        City= request.POST.get('City')
        State = request.POST.get('State')
        Pin = request.POST.get('Pin')
        Phone = request.POST.get('Phone')
        contact = Contact(firstname=firstname,lastname=lastname,email=email,City=City,State=State,Pin=Pin,Phone=Phone,Date=datetime.today())
        contact.save()
    templates = 'contact.html'
    return render(request,templates)
    # return HttpResponse("this is contact page") 