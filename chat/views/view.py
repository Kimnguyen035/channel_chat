from rest_framework.viewsets import ViewSet
from helpers.respone import *
from django.shortcuts import render

class VView(ViewSet):
    def index(request):
        return render(request, 'chat/index.html')
    
    def room(request, room_name):
        return render(request, "chat/room.html", {"room_name": room_name})