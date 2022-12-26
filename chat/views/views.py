from rest_framework.viewsets import ViewSet
from helpers.respone import *

class VView(ViewSet):
    def hello_world(self, request):
        hw = 'Hello world'
        return response_data(hw)