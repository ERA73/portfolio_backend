from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

def register_app_models(name):
    app_models = apps.get_app_config(name).get_models()
    loaded = 0
    ignored = 0
    for model in app_models:
        try:
            admin.site.register(model)
            loaded += 1
        except AlreadyRegistered:
            ignored += 1
    return f"loaded:{loaded}, ignored:{ignored}"