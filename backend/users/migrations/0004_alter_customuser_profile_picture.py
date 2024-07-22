# Generated by Django 4.2.14 on 2024-07-19 15:21

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_images/default_profile.jpg', null=True, upload_to=users.models.user_profile_picture_file_path),
        ),
    ]