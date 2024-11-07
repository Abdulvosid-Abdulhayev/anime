from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    # `dictionary` lug'at ekanligiga ishonch hosil qilish uchun tekshirish
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None
