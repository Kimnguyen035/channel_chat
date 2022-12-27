from django.urls import path
from .views.room_view import RoomView

all_url = {
    'test': [
        path('', RoomView.index, name='index'),
        path('chat/<str:room_name>/', RoomView.room, name='room'),
    ],
}

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]