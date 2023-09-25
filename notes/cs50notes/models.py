from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Course (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
    
       return self.name
       
 # Define a LectureNote model to store individual lecture notes.
class LectureNote(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank = True, null = True )
    category = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=100, default='python')
    web_link = models.URLField(blank=True, null=True)
    
    
   

    def __str__(self):
        return self.title      