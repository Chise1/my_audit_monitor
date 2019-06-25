from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from node.models import CaseNode


class Member(models.Model):
    """
    用户
    继承于AbstractUser，带了基本的User字段
    """
    user = models.OneToOneField(User, models.CASCADE, null=True, blank=True, related_name="member")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    nodes=models.ManyToManyField(CaseNode,verbose_name="跟随节点",related_name="User_Node")
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name is None:
            return ""
        else:
            return self.name

