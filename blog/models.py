from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 63)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title

