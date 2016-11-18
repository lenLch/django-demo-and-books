from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader,RequestContext

from books import models

# Create your views here.

def show(request):
#    publisher_list = [{'name':"gongye",'city':'beijing'}]
#    publisher_list = models.Publisher.objects.all()
#    publisher_list = models.Publisher.objects.values('name','city')

#    models.Publisher.objects.filter(id=1).update(city="Chengdu")
#    publisher_list = models.Publisher.objects.get(id=1)
#    publisher_list.city = "shenzhen"
#    publisher_list.save()
    
    models.Publisher.objects.filter(id=1).delete()
    publisher_list = models.Publisher.objects.get(id=2)
    

    return render_to_response('show.html',{'publisher_list':publisher_list})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = models.Book.objects.filter(title__icontains = q)
        return render_to_response('search_results.html',{'books':books,'query':q})
    else:
        return render_to_response('search_form.html',{'error':True})

    
def search1(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Enter a search form")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters")
        else:

            books = models.Book.objects.filter(title__icontains = q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    
    return render_to_response('search_form1.html',{'errors':errors})


#def foo_view(request):
#    return render_to_response('template1.html',{'name':"FOO"})
#def bar_view(request):
#    return render_to_response('template2.html',{'name':"BAR"})
#def foobar_view(request,url):
#    if url == 'foo':
#        return render_to_response('template1.html',{'name':"FOO"})
#    elif url == 'bar':
#        return render_to_response('template2.html',{'name':"BAR"})

def foobar_view(request,template_name):
        return render_to_response(template_name,{'name':"FOO"})

def custom_proc(request):
    return {'app':'My app','user':'lvze','ip_address':'192.168.1.3:8888'}

def view(request):
#    t = loader.get_template('view.html')
#    c = RequestContext(request,{'message':'I am view'},processors = [custom_proc])
#    return HttpResponse(t.render(c))
    return render_to_response('view.html',{'message':"I am view"},context_instance = RequestContext(request,processors=[custom_proc]))
