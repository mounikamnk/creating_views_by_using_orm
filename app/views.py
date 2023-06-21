from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(self):
    tn=input('enter topic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('this is topic page')
def insert_webpage(self):
    tn=input('enter topic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('this is webpage')
def insert_AccessRecord(self):
    tn=input('entertopic')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('entername')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter date')
    a=input('enter name')
    AR=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AR.save()
    return HttpResponse('this is Access record page')

