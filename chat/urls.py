from django.urls import path
from .views.view import *

all_url = {
    'test': [
        path('hello_world', VView.as_view({'get':'hello_world'})),
        path('', VView.index, name='index'),
    ],
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]