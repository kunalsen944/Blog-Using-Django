# Generated by Django 2.1.1 on 2018-10-11 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0013_auto_20181011_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]