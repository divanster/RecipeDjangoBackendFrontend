# Generated by Django 4.2.14 on 2024-07-19 15:21

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default='default_images/default_recipe.jpeg', null=True, upload_to=recipes.models.recipe_image_file_path),
        ),
    ]