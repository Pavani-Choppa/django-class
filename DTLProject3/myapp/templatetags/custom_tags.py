from django import template

register = template.Library()

@register.simple_tag
def make_upper(name):
    return name.upper()

@register.simple_tag
def greet(name):
    return f"Hello, {name}!"

@register.simple_tag
def custsom_tag_fun():
    return "Welcome to Custom tags Excercide"

@register.simple_tag
def add_fun(n1,n2):
    return n1+n2

@register.filter
def list_sum(numbers):
    return sum(numbers)

@register.filter
def even_index_sum(numbers):
    total = 0

    for i in range(0, len(numbers), 2):
        if numbers[i] % 2 == 0:
            total += numbers[i]

    return total
