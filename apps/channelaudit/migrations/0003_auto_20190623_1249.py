# Generated by Django 2.2.1 on 2019-06-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channelaudit', '0002_auto_20190623_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseprojectdevice',
            name='device_name',
            field=models.CharField(default=1, max_length=128, verbose_name='设备名称'),
            preserve_default=False,
        ),
    ]
