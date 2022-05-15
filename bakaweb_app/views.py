from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .api import BakConnection

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'bakaweb_app/index.html'

    def post(self, request):
        input = request.POST
        connection = BakConnection(input['url'], input['user'], input['pw'])
        return render(request, self.template_name, {"subjects": connection.marks()})