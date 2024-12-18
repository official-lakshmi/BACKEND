from django.db import models
from django.contrib.auth.models import User

# models for videos
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField()  
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Staff member who uploaded the video
    
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Make it nullable

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Document Model
class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')  # Location where documents will be stored
    
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Make it nullable
#  uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Staff member who uploaded the document
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title