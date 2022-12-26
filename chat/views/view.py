from rest_framework.viewsets import ViewSet
from helpers.respone import *
from django.shortcuts import render

class VView(ViewSet):
    def hello_world(self, request):
        hw = 'Hello world'
        return response_data(hw)
    
    def index(request):
        return render(request, 'chat/index.html')