from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), 'baka'),
    path('test/', test, name='test'),
    path('marks/', marks, name='marks'),
    path('timetable/', timetable, name='timetable'),
]

