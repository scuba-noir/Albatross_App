from django.shortcuts import render, redirect
from albatross_app.forms import contactForm

def index(request):

    return redirect(homepage)

def homepage(request):

    context = {}

    if request.method == "POST":

        form_post = contactForm(request.POST)

        if form_post.is_valid():
            
            form_post.data = form_post.cleaned_data
            form_post.full_clean()
            form_post.save()

            return redirect('homepage')

    else:

        form_1 = contactForm()
        context['contact_form'] = form_1

    return render(request, 'pages/homepage.html', context = context)

def user_login(request):

    context = {}
    return render(request, 'pages/login.html', context = context)

def user_profile(request):

    context = {}
    return render(request, 'pages/user_profile.html', context = context)

def about(request):
    
    context = {}
    return render(request, 'pages/about.html', context = context)

def technology(request):
    
    context = {}
    return render(request, 'pages/technology.html', context = context)

def merch_tent(request):
    
    context = {}
    return render(request, 'pages/merch_tent.html', context = context)