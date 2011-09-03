#coding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from forms import SubscriptionForm
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from subscription.models import Subscription

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context=RequestContext(request, {'subscription':subscription})
    return render_to_response('salvo.html',context)

def new(request):
    form = SubscriptionForm(initial={
                'name':'Digite seu nome completo',
                'cpf': 'Digite seu cpf',
                'email':'Informe seu email',
                })
    context = RequestContext(request, {'form':form})
    return render_to_response('new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        context = RequestContext(request, {'form':form})
        return render_to_response('new.html', context)
    
    
    subscription = form.save()
        
    send_mail(subject=u'Inscrição no EventeX',
           message=u'Obrigado(a) por se inscrever no EventeX!',
           from_email=u'contato@eventex.com', 
           recipient_list = [ 'luizfernandorg@gmail.com', ])
    return HttpResponseRedirect(reverse('subscription:success', args=[subscription.pk]))
