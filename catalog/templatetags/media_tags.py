from django import template
from django.conf import settings

register = template.Library()

@register.filter
def mediapath(path):
    if path:
        return f"{settings.MEDIA_URL}{path}"
    return ""

@register.simple_tag
def media_url():
    """Тег для получения базового URL медиафайлов"""
    return settings.MEDIA_URL

