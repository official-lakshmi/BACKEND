from rest_framework import serializers
from .models import Video,Document


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_url', 'uploaded_by', 'created_at', 'updated_at']
        # fields = ['id', 'title', 'description', 'video_url',  'created_at', 'updated_at']



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        # fields = ['id', 'title', 'description', 'file', 'created_at', 'updated_at']
        fields = ['id', 'title', 'description', 'file', 'uploaded_by', 'created_at', 'updated_at']