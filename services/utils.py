# -*- coding: utf-8 -*-

from django.utils import timezone
from django.apps import apps
from management.models import Resident


def get_model_name(item_alias):
    return ''.join([word.capitalize() for word in item_alias.split('_')])


def get_model(type_alias, item_alias):
    model_name = get_model_name(item_alias)
    return apps.get_model(app_label=type_alias, model_name=model_name)


def get_resident(request):
    resident_id = request.session.get('resident_id')
    return Resident.objects.get(id=int(resident_id))


def new_year_day():
    return timezone.now().date().replace(month=1, day=1)
