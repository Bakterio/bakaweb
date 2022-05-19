from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .api import BakConnection
from .forms import *

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'bakaweb_app/index.html'

    def post(self, request):
        input = request.POST
        connection = BakConnection(input['url'], input['user'], input['pw'])
        if (connection != None):
            return render(request, 'bakaweb_app/marks.html', {"subjects": connection.marks()})

def test(request):
    form = LoginForm(request.POST or None)
    return render(request, 'bakaweb_app/test.html', {'form': form})