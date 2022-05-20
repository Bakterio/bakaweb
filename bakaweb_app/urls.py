from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('test/', test),
    path('marks/', marks),
    path('timetable/', timetable),
]

