from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from requests.sessions import session
from .api import BakConnection
from .forms import *

def check_session(request):
    for i in ('url', 'user', 'pw'):
        if request.session[i] == None:
            return None

class IndexView(generic.TemplateView):
    template_name = 'bakaweb_app/index.html'

    def post(self, request):
        input = request.POST
        connection = BakConnection(input)
        if (connection != None):
            for i in ('url', 'user', 'pw'):
                request.session[i] = input[i]

            return redirect('/marks')

    def delete(self, request):
        for i in ('url', 'user', 'pw'):
            request.session[i] = None

def test(request):
    form = LoginForm(request.POST or None)
    return render(request, 'bakaweb_app/test.html', {'form': form})

def marks(request):
    if check_session(request) == None:
        redirect(reverse('baka'))
    return render(request, 'bakaweb_app/marks.html', {'subjects': BakConnection(request.session).marks()})

def timetable(request):
    return render(request, 'bakaweb_app/timetable.html', {'timetable': BakConnection(request.session).timetable()})

