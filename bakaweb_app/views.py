from django.shortcuts import render, redirect
from django.views import generic
from .api import BakConnection
from .forms import *

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'bakaweb_app/index.html'

    def post(self, request):
        input = request.POST
        connection = BakConnection(input)
        if (connection != None):
            for i in ('url', 'user', 'pw'):
                request.session[i] = input[i]

            return redirect('/marks')

def test(request):
    form = LoginForm(request.POST or None)
    return render(request, 'bakaweb_app/test.html', {'form': form})

def marks(request):
    return render(request, 'bakaweb_app/marks.html', {'subjects': BakConnection(request.session).marks()})

def timetable(request):
    return render(request, 'bakaweb_app/timetable.html', {'timetable': BakConnection(request.session).timetable()})
