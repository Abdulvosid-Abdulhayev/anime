from django import template
from django.shortcuts import get_object_or_404
from ..models import Anime, Category

register = template.Library()

@register.inclusion_tag('categories.html', takes_context=True)
def display_categories(context, slug=None):
    # Fetch all categories
    categories = Category.objects.all()

    # Determine the anime queryset based on slug
    if slug:
        category = get_object_or_404(Category, slug=slug)
        animes = Anime.objects.filter(category=category)
    else:
        animes = Anime.objects.all()

    # Update context with animes and categories
    context.update({
        'categories': categories,
        'animes': animes,
        'selected_category': category if slug else None
    })
    return context
