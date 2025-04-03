from django.shortcuts import render

# Create your views here.
def req(request):
    return render(request,'basic.html')