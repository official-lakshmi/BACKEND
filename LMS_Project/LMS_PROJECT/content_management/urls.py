from django.urls import path
from .views import VideoUploadView,DocumentUploadView

urlpatterns = [
    path('upload-video/', VideoUploadView.as_view() , name = 'upload-video'),
    path('upload-document/', DocumentUploadView.as_view(), name='upload-document'),

]
