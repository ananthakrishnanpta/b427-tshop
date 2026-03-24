from django.shortcuts import render

# Create your views here.

def homeView(request):
    template = 'mainapp/home.html'

    return render(
        request = request,
        template_name= template,
        context={}
    )

def aboutView(request):
    template = 'mainapp/about.html'

    return render(
        request = request,
        template_name= template,
        context={}
    )

def contactView(request):
    template = 'mainapp/contact.html'

    return render(
        request = request,
        template_name= template,
        context={}
    )