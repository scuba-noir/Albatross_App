from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, FileResponse
from albatross_app.forms import contactForm
from albatross_site import settings
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

import os



def index(request):

    return redirect(homepage)

@csrf_protect
def homepage(request):

    context = {}

    if request.method == "POST":

        form_post = contactForm(request.POST)

        if form_post.is_valid():
            
            form_post.data = form_post.cleaned_data
            email_string = "Email: " + str(form_post.data['email']) + "\n" + "Message: " + str(form_post.data['message'])
            form_post.full_clean()
            form_post.save()
            print(form_post.data)
            send_mail(
                subject='New Contact Form Submission',
                message=email_string,
                from_email="cthompson@albatrossgolf.io",
                recipient_list=['cthompson@albatrossgolf.io','nickmills@albatrossgolf.io','timothymusick@albatrossgolf.io ']
            )

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

def open_file(request):

    file_path = 'staticfiles/assets/pdf/albatross_whitepaper.pdf'
    print(os.getcwd())
    print(file_path)
    file = open(file_path, 'rb')
    return FileResponse(file, as_attachment=True, filename='albatross_whitepaper.pdf')
  