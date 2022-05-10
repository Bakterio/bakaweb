from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import api

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'bakaweb_app/index.html'

    def post(self, request):
        input = request.POST
        token = api.get_token(input['url'], input['user'], input['pw'])
        data = api.znamky(input['url'], token)
        #   return render(request, self.template_name, {"out": api.znamky(input['url'], token)})
        return HttpResponse(data)