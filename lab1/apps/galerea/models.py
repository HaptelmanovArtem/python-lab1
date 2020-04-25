from django.db import models

class Image(models.Model):
    image_title = models.CharField('image name', max_length=100)
    image_url = models.CharField('image', max_length=10000)
    image_like = models.IntegerField('count like')

    def __str__(self):
        return self.image_title

    def getImage(self):
        return self
