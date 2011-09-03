# -*- coding: utf-8 -*-

from django.forms import ModelForm
from subscription.models import Subscription
from django import forms
from django.utils.translation import ugettext as _
from django.core.validators import EMPTY_VALUES

class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (forms.TextInput(attrs=attrs),
                   forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)
        
    def decompress(self, value):
        if not value:
            return [None, None]
        print "Retorno em decompress = ", value.split('-')
        return value.split('-')
    
class PhoneField(forms.MultiValueField):
    widget = PhoneWidget
    
    def ___init__(self, *args, **kwargs):
        fields = (forms.IntegerField(),
                  forms.IntegerField())
        super(PhoneField, self).___init__(fields, *args, **kwargs)
        
    def compress(self, data_list):
        if not data_list:
            return None
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(u'DDD inválido.')
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(u'Número inválido.')
        print "Retorno em compress = ", data_list
        return "%s-%s" % tuple(data_list)
    
class SubscriptionForm(ModelForm):
    phone = PhoneField(required=False)
    
    class Meta:
        model = Subscription
        exclude = ('created_at','paid',)
    
    def clean(self):
        super(SubscriptionForm, self).clean()
        print self.cleaned_data
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise forms.ValidationError(_(u'Informe seu e-mail ou telefone.'))
        
        return self.cleaned_data

