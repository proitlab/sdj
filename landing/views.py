from django.shortcuts import render
from django.views.generic import ListView
from data.models  import Anggota
from django.db.models import Q

def index(request):
    return render(request, 'landing/index.html')

class IndexView(ListView):
    model = Anggota
    template_name = 'landing/index.html'
    
    #queryset = Anggota.objects.filter(name__icontains='Dedy') # new

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            object_list = Anggota.objects.filter(
                Q(nama_anggota__icontains=query) | Q(nomor_anggota__icontains=query)
            )
            return object_list