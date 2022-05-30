from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
# Create your views here.


class WelcomePage(APIView):
    def get(self, request):
        return HttpResponse('Greetings.....!')
    