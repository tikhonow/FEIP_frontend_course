from django.db import models


# Create your models here.
def image_folder(instance, filename):
    return '/'.join(['avatars', filename])


# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return self.name
