from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# def index(request):
#     return HttpResponse("Eia plataforma")
class Create_machine(APIView):
    def post(self, request):
        return Response (status=status.HTTP_200_OK)

class Create_machine(APIView):
    def get(self, request):
        return Response (status=status.HTTP_200_OK)
