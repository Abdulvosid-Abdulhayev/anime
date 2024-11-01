from django.contrib import admin
from .models import Category, Anime, Episode, Coments

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 0 
    fields = ("episode_number", "title", "video_file")

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "release_date", "episode_count", "views", "coments_count", "price", "header_publish")
    search_fields = ("title", "description", "slug")
    list_filter = ("release_date", "category")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("category",)
    readonly_fields = ("views", "coments_count")
    inlines = [EpisodeInline]  
    fieldsets = (
        ("Asosiy Ma'lumotlar", {
            "fields": ("title", "slug", "description", "category", "release_date", "episode_count", "price", "header_publish")
        }),
        ("Rasm", {
            "fields": ("cover_image", "header_image"),
        }),
        ("Statistika", {
            "fields": ("views", "coments_count"),
            "classes": ("collapse",),
        }),
    )
    

# Category modeli uchun admin sozlamalari
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

# Coments modeli uchun admin sozlamalari
@admin.register(Coments)
class ComentsAdmin(admin.ModelAdmin):
    list_display = ("name", "anime", "created_at")
    search_fields = ("name", "text")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
