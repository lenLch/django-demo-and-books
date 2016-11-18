#coding=utf-8
from django.http import HttpResponse
import datetime

from django.template import loader
from django.shortcuts import render,render_to_response

def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse("你好")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)

def hour_ahead(request,offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s),it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)

def xiaomi(request):
    t = loader.get_template("xiaomi.html")
    html = t.render({})
    return HttpResponse(html)

d = {'name':'zhangsan','age':'14'}
l = ['zhangsan','14']
class A:
    age = 1

a = A()

def fun():
    return "hello"
'''
def name(request):

    today = 0
#    name_list = ['zhanngsan','lisi','wangwu']
    name_list = []

    t = loader.get_template("name.html")
#    html = t.render({'name':'lvze'})
    html = t.render({'name':fun,'today_is_weekend':today,'athlete_list':name_list})
    return HttpResponse(html)
'''    

def name(request):

    today_is_weekend = 0
    athlete_list = ['zhanngsan','lisi','wangwu']
    name = "zhangsan"


#    t = loader.get_template("name.html")
#    html = t.render({'name':fun,'today_is_weekend':today,'athlete_list':name_list})
#    return HttpResponse(html)
#    return render_to_response('name.html',{'name':fun,'today_is_weekend':today,'athlete_list':athlete_list})
    return render_to_response('name.html',locals())#{'today_is_weekend':today_is_weekend,'athlete_list':athlete_list,'name':name}

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    path = request.path
    for (k,v) in values:
        html.append((k,v))
    return render_to_response('meta.html',{'meta_data':html,'request_path':path})
