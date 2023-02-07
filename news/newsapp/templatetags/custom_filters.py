from django import template

register = template.Library()

STOP_LIST = [
    'что',
    ]

@register.filter(is_safe=True)
def censor(value):
    STOP_LIST = ['что', 'почему']

    if not isinstance(value, str):
        raise TypeError(f"Недопустимое значение '{type(value)}' Нужно ввести строковое значение")

    for word in value.split():
        if word.lower() in STOP_LIST:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value
