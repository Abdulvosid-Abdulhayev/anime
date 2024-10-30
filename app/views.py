from django.shortcuts import render
from django.views import View
from .models import*
# Create your views here.

class Home(View):
    def get(self, request):
        animes = Anime.objects.all()
        context = {
            "animes": animes,
        }
        return render(request, 'index.html', context=context)