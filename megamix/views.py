from django.shortcuts import render,HttpResponse
from .models import *
from .form import message_form


def homepage(request):
    return render(request, 'index.html',
                  context={'works': project.objects.all(), 'programmers': member.objects.all()})


def contact_page(request):
    if request.method == 'GET':
        form = message_form()
        return render(request, 'contact.html', {'form': form})
    else:
        form = message_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            customer_message.objects.create(name=data['name'], message=data['message'], subject=data['subject'],
                                            email=data['email'])
        return render(request, 'contact.html', {'form': form})
