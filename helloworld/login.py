from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request,'index.html')

def login_search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '搜索的内容为' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)