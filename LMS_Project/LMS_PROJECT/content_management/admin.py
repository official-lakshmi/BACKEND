from django.contrib import admin
from .models import Video, Document

# Registering the Video model with the Django Admin interface
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'created_at', 'updated_at')  # Display these fields in the admin list view
    # list_display = ('title', 'created_at', 'updated_at')  # Display these fields in the admin list view
    search_fields = ('title', 'description')  # Allow searching by title and description

# Registering the Document model with the Django Admin interface
class DocumentAdmin(admin.ModelAdmin):
    # list_display = ('title',  'created_at', 'updated_at')  # Display these fields in the admin list view
    list_display = ('title', 'uploaded_by', 'created_at', 'updated_at')  # Display these fields in the admin list view
    search_fields = ('title', 'description')  # Allow searching by title and description

# Register the models so they appear in the Django Admin panel
admin.site.register(Video, VideoAdmin)
admin.site.register(Document, DocumentAdmin)
