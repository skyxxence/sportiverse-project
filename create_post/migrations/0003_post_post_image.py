# Generated by Django 5.1.1 on 2024-10-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_post', '0002_rename_post_name_post_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.CharField(blank=True, null=True),
        ),
    ]
