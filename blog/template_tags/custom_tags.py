from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def multiply(a, b):
    # you would need to do any localization of the result here
    return a * b