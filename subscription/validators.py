# coding:utf-8

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

def cpf_valitador(value):
    if not value.isdigit():
        raise ValidationError(_(u"O CPF deve conter somente números"))
    
    if len(value) != 11:
        raise ValidationError(_(u"Cpf precisar ter 11 digitos!"))
