from django import template

register = template.Library()


@register.simple_tag
def digits_to_persian_numbers(target):
    target = list(target)
    english_digits_code_list = [ord(num) for num in list("0123456789")]
    persian_digits_code_list = list("۰۱۲۳۴۵۶۷۸۹")
    for index, character in enumerate(target):
        if ord(character) in english_digits_code_list:
            target[index] = persian_digits_code_list[int(character)]
    target = "".join(target)
    return target
