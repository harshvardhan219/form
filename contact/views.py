from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


# Create your views here.

from .forms import ContactForm
from .models import Contact


def contact(request):
    templates = 'contact.html'

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, templates, context)
