from django import template
from datetime import datetime
register = template.Library()

@register.filter
def calculo_duracao(value1, value2):
    if isinstance(value1, datetime) and isinstance(value2, datetime):
        return f"{(value1 - value2).days} dias"
         
    return "Ainda não houve a devolução"