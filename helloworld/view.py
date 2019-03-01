from django.shortcuts import render
from . import testdb

def hello(request):
    context ={}
    test123=testdb.testdb(request)
    context['hello']=test123
    return render(request,'helloworld.html',context)