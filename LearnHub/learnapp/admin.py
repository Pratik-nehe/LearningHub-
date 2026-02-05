from django.contrib import admin
from .models import *  # imports all models from this app

from django.apps import apps
app_models = apps.get_app_config('learnapp').get_models()

for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


admin.site.site_header="Learninghub Admin"
admin.site.site_title="Learninghub admin login"
admin.site.index_title="WelCome To Learninghub"
