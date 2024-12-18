from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Video, Document
from .serializers import VideoSerializer, DocumentSerializer


# remove this after setting the permission
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
# till here


# Video upload view
class VideoUploadView(APIView):

    # uncomment this    NO.1
    # permission_classes = [IsAuthenticated]  # Only authenticated staff can upload videos

    authentication_classes = []  # Disable authentication
    permission_classes = [AllowAny]  # Allow any user

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            # uncomment this    NO.2
            # serializer.save(uploaded_by=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Document upload view
class DocumentUploadView(APIView):

    # uncomment this    
    # permission_classes = [IsAuthenticated]  # Only authenticated staff can upload documents

    authentication_classes = []  # Disable authentication
    permission_classes = [AllowAny]  # Allow any user

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            # uncomment this 
            # serializer.save(uploaded_by=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)