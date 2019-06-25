from django.db import models

class SensetimeID(models.Model):
    name = models.CharField(null=True, max_length=128, verbose_name="秘钥名称")
    ak = models.CharField(max_length=128, verbose_name="AK")
    sk = models.CharField(max_length=128, verbose_name="SK")

    class Meta:
        verbose_name = "商汤SID"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id

