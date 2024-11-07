from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Count, Q
from .models import Anime, Category, Coments

# Kategoriya bo‘yicha anime sonlarini olish funksiyasi
def get_category_count():
    categories = Category.objects.annotate(anime_count=Count('anime'))
    category_count = {category.name: category.anime_count for category in categories}
    return category_count

from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import Anime, Category

class SearchView(View):
    def post(self, request):
        query = request.POST.get('q', '')  # `q` ni `POST` so‘rovidan olish
        if query:
            # Faqat noyob `title` bo‘yicha `distinct()` qilish
            animes = Anime.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            ).distinct()  # Unikal natijalarni olish uchun `distinct()`
        else:
            animes = Anime.objects.none()  # Qidiruv bo‘lmasa, bo‘sh natija qaytariladi
        category_count = get_category_count()
        categories = Category.objects.all()
        context = {
            "animes": animes,
            "categories": categories,
            "query": query,
            "category_count": category_count,
            
        }
        return render(request, 'search_results.html', context=context)


class Home(View):
    def get(self, request):
        animes = Anime.objects.all()
        categories = Category.objects.all()
        category_count = get_category_count()

        context = {
            "animes": animes,
            "categories": categories,
            "category_count": category_count,
        }
        return render(request, 'index.html', context=context)

class Caregory(View):
    def get(self, request, slug=None):
        categories = Category.objects.all()
        category_count = get_category_count()

        if slug:
            category = get_object_or_404(Category, slug=slug)
            animes = Anime.objects.filter(category=category)
            selected_category = category
        else:
            animes = Anime.objects.all()
            selected_category = "All"

        context = {
            "animes": animes,
            "categories": categories,
            "selected_category": selected_category,
            "category_count": category_count,
        }
        return render(request, 'categories.html', context=context)

class Anime_detail(View):
    def get(self, request, selected_category, slug):
        anime = get_object_or_404(Anime, slug=slug)
        categories = Category.objects.all()
        category_count = get_category_count()
        anime_4 = Anime.objects.order_by("?")[:4]
        comments = Coments.objects.filter(anime=anime).order_by('-created_at')

        # Ko'rishlar sonini oshirish
        anime.views += 1
        anime.save()

        context = {
            "anime": anime,
            "categories": categories,
            "selected_category": selected_category,
            "anime_4": anime_4,
            "comments": comments,
            "category_count": category_count,
        }
        return render(request, 'anime-details.html', context=context)

class Login(View):
    def get(self, request):
        categories = Category.objects.all()
        category_count = get_category_count()

        context = {
            "categories": categories,
            "category_count": category_count,
        }
        return render(request, 'login.html', context=context)
