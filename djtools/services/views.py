from django.views.generic import ListView, DetailView

from .models import Service


class ServicesView(ListView):
    model = Service
    template_name = 'djtools/services/service_list.html'

    def get_queryset(self):
        return Service.objects.filter(active=True)


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'djtools/services/service_detail.html'
