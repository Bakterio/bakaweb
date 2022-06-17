from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.core.mail import send_mail
from .api import BakConnection
from .forms import *

def check_session(request):
    for i in ('url', 'user', 'pw'):
        if not i in request.session:
            return True

class IndexView(generic.TemplateView):
    template_name = 'bakaweb_app/index.html'

    def post(self, request):
        input = request.POST
        connection = BakConnection(input)
        if (connection != None):
            for i in ('url', 'user', 'pw'):
                request.session[i] = input[i]

        return redirect(reverse('timetable'))

def test(request):
    form = LoginForm(request.POST or None)
    return render(request, 'bakaweb_app/test.html', {'form': form})

def marks(request):
    if check_session(request):
        return redirect(reverse('baka'))
    return render(request, 'bakaweb_app/marks.html', {'subjects': BakConnection(request.session).marks()})

def timetable(request):
    if check_session(request):
        return redirect(reverse('baka'))
    return render(request, 'bakaweb_app/timetable.html', BakConnection(request.session).timetable())

def logout(request):
    if check_session(request):
        return redirect(reverse('baka'))
    for i in ('url', 'user', 'pw'):
        del request.session[i]
    return redirect(reverse('baka'))
