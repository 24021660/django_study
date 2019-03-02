from django.shortcuts import render_to_response,render
from django.http import HttpResponse

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message='搜索的内容为'+request.GET['q']
    else:
        message='你提交了空表单'
    return HttpResponse(message)

def search_form(request):
    return render_to_response('index.html')

def post_form(request):
    ctx={}
    if request.POST:
        ctx['rlt']=request.POST['q']

    return render(request,'post.html',ctx)