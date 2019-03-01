from django.shortcuts import render

def hello(request):
    context ={}
    context['hello']='helloworld!!!'
    return render(request,'helloworld.html',context)