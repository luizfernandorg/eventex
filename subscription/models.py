# coding:utf-8
from django.db import models
from django.utils.translation import ugettext as _
from subscription import validators

class Subscription(models.Model):
    name = models.CharField(_("Nome"),max_length=100)
    cpf = models.CharField(_("CPF"),max_length=11, unique=True, validators=[validators.cpf_valitador])
    email = models.EmailField(_("E-mail"), unique=True, blank=True)
    phone = models.CharField(_("Telefone"),max_length=20, blank=True)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    paid = models.BooleanField(_("Pago"))
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["paid"]
        verbose_name = u'Inscrição'
        verbose_name_plural = u'Inscrições'
