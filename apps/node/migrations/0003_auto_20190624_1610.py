# Generated by Django 2.2.1 on 2019-06-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0002_auto_20190623_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casenode',
            name='fly_sheet_audit_tolerance',
            field=models.IntegerField(default=30, verbose_name='稽核时间容差，单位min'),
        ),
    ]
