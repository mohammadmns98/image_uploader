from django.db import models
from django.conf import settings

# class ImageModel(models.Model):
#     user = models.ForeignKey(
#         User, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

class ImageModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    caption = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
