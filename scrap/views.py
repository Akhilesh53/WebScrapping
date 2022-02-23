import os
from django.shortcuts import render
from numpy import imag
from . serializers  import ScrapSerializer
from rest_framework.response import Response
from .models import ScrapModel
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from rest_framework import status
from rest_framework.response import Response
from .models import ScrapModel
from .serializers import ScrapSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
import sys

sys.path.append('C:\\Users\\akhil\\OneDrive\\Documents\\outsidefolder')

from Global.ScrapDetails import scrapdetails

class scrap_list(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        snippets = ScrapModel.objects.all()
        serializer = ScrapSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ScrapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class scrap_detail(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        #data=request.data
        #snippet = ScrapModel.objects.get(id=data['id'])
        #serializer = ScrapSerializer(snippet)
        #filename=serializer.data['filename']+'.py'
        #exec(open(os.getcwd()+'\\Data\\'+filename).read())
        scrapdetails(data=request.data,model=ScrapModel,serailizer=ScrapSerializer)
        return Response("Scrapping Done", status=status.HTTP_201_CREATED)

