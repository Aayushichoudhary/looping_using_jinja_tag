from django.shortcuts import render

# Create your views here.


def forloop(request):
    d={'num':range(12321)}
    return render(request,'forloop.html',context=d)