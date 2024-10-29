from django.db import models

class Comment(models.Model):
    post_name = models.CharField(max_length=200)
    post_body = models.TextField(null=True, blank= True)
    pass

# Create your models here.
