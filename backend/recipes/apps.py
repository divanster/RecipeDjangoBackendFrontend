from django.apps import AppConfig

class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
    verbose_name = 'Recipes'

    # def ready(self):
    #     import recipes.signals  # Import signals if you have any
