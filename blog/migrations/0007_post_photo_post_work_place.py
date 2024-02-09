# Generated by Django 5.0.1 on 2024-02-08 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
        migrations.AddField(
            model_name='post',
            name='work_place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]