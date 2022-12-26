from django.urls import path
from .views.view import *

all_url = {
    'test': [
        path('', VView.index, name='index'),
        path('chat/<str:room_name>/', VView.room, name='room'),
    ],
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]