from django.core.mail import send_mail, BadHeaderError, mail_admins
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        f = ContactusForm(request.POST)
        if f.is_valid():
            first_name = f.cleaned_data['first_name']
            last_name = f.cleaned_data['last_name']
            sender = f.cleaned_data['email']
            subject = "You have a new message from {}:{}".format(last_name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)

            f.save()
            messages.add_message(request, messages.INFO, 'votre message a été envoyer avec success.')
            return redirect('contact')
    else:
        f = ContactusForm()
    context = {
        'imgas': Myimgacceuil.objects.all(),
        'abouts': Aboutme.objects.all(),
        'works': Work.objects.all(),
        'dcoder': Dcoder.objects.all(),
        'gallerys': Gallery.objects.all(),
        'progs': Prog.objects.all(),
    }
    return render(request, 'portfolio/index.html',context)
