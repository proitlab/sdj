from data.models import Anggota, Keluarga
from django.contrib import admin
from django.urls import path
from dashboard.models import *
from dashboard.views import *
from django.template.response import TemplateResponse

# Register your models here.
class DashboardAdmin(admin.ModelAdmin):

    template_name = 'dashboard/index.html'

    def get_urls(self):
        dashboard_view = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            #path('', DashboardView, name=dashboard_view),
            path('', self.dashboard_view, name=dashboard_view),
        ]

    def dashboard_view(self, request):
        context = {
            **self.admin_site.each_context(request),
            'dashboard_title': 'Dashboard',
            'total_jemaat': Anggota.objects.count(),
            'total_keluarga': Keluarga.objects.count(),
        }

        return TemplateResponse(request, self.template_name, context)

admin.site.register(Dashboard, DashboardAdmin)
