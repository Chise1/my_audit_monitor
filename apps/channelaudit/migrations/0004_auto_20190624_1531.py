# Generated by Django 2.2.1 on 2019-06-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channelaudit', '0003_auto_20190623_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseproject',
            name='group_id',
            field=models.CharField(default=2500000000, max_length=32, verbose_name='项目GROUP_ID'),
            preserve_default=False,
        ),
    ]