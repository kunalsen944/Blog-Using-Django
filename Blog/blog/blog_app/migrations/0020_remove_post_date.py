# Generated by Django 2.1.1 on 2018-10-15 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0019_auto_20181015_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
