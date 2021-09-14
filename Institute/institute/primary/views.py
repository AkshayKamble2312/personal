from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('this is index page')
    return render(request,'index.html')


def test(request):
    return HttpResponse('this is test page')
