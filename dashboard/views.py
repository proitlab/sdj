'''
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.models import Dashboard
from django.template.response import TemplateResponse

def DashboardView(request):
    template = 'dashboard/index.html'
    context = {
        'total_anggota': 99,
        'total_simpatisan': 9
        }
    return TemplateResponse(request, template, context)
    #return render(request, template, context)
    #return HttpResponse('Admin Custom View')
    '''
    