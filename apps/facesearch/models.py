from django.db import models

# Create your models here.
from channelaudit.models import CaseProject


class FaceSearch(models.Model):
    image = models.ImageField(upload_to="FaceSearchFiles")
    project=models.ForeignKey(CaseProject,models.CASCADE)
    first_look=models.DateTimeField(null=True,blank=True)
    class Meta:
        verbose_name="人脸搜索"
        verbose_name_plural=verbose_name