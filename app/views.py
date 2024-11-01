from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import*
# Create your views here.

class Home(View):
    def get(self, request):
        animes = Anime.objects.all()
        categories = Category.objects.all()

        context = {
            "animes": animes,
            "categories": categories,
        }
        return render(request, 'index.html', context=context)
    

class Caregory(View):
    def get(self, request, slug=None):
        # Initialize categories first to avoid UnboundLocalError
        categories = Category.objects.all()

        if slug is None:
            animes = Anime.objects.all()
            category = "All"
            context = {
                "animes": animes,
                "categories": categories, 
                "selected_category": category,
            }
        else:
            # Use get_object_or_404 to fetch the category safely
            category = get_object_or_404(Category, slug=slug)
            animes = Anime.objects.filter(category=category)
            context = {
                "animes": animes,
                "categories": categories,
                "selected_category": category
            }

        return render(request, 'categories.html', context=context)


class Anime_detail(View):
    def get(self, request, slug, selected_category=None):
        print(selected_category=="All")
        # Anime ob'ektini olish
        if selected_category=="All":
            anime = get_object_or_404(Anime, slug=slug)
            categories = Category.objects.all()
            anime_4 = Anime.objects.order_by("?")[:4]
            category = None
            anime.views += 1
            anime.save()

            # Anime ob'ektining kategoriyasini selected_category sifatida olish
            
            context = {
                "anime": anime,
                "categories": categories,
                "selected_category": selected_category,
                "category": category,
                "anime_4": anime_4,
            }
        else:
            anime = get_object_or_404(Anime, slug=slug)
            categories = Category.objects.all()
            anime_4 = Anime.objects.order_by("?")[:4]
            category = get_object_or_404(Category,name=selected_category)
            anime.views += 1
            anime.save()

            # Anime ob'ektining kategoriyasini selected_category sifatida olish
            
            context = {
                "anime": anime,
                "categories": categories,
                "selected_category": selected_category,
                "category": category,
                "anime_4": anime_4,
            }
        return render(request, 'anime-details.html', context=context)
    
class Coment(View):
    def post(self, request):
        coment_text = request.GET.get("coment_text")
        anime_id = request.GET.get("anime_slug")
        