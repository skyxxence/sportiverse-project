from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField(null=True, blank= True)
    post_image = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return self.post_title

