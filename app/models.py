from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=100, verbose_name="Slug")

    
    class Meta:
        verbose_name_plural = 'Kategoriyalar'
        verbose_name = "Kategoriya"
    
    def __str__(self):
        return self.name
    




class Anime(models.Model):
    title = models.CharField(max_length=255, verbose_name="Anime nomi")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    description = models.TextField(verbose_name="Ma'lumot")
    category = models.ManyToManyField(Category, verbose_name="Kategoriya")
    release_date = models.DateField(verbose_name="Chiqarilgan sana")
    episode_count = models.PositiveIntegerField(verbose_name="Qismlar soni", default=0)
    cover_image = models.ImageField(upload_to="anime/covers/", verbose_name="Rasm")
    views = models.IntegerField(default=0)
    coments_count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Animelar"

class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name="episodes", verbose_name="Anime")
    title = models.CharField(max_length=255, verbose_name="Epizod nomi")
    video_file = models.FileField(upload_to="anime/videos/", verbose_name="Video fayl")
    episode_number = models.PositiveIntegerField(verbose_name="Epizod raqami")

    def __str__(self):
        return f"{self.anime.title} - Epizod {self.episode_number}"

    class Meta:
        verbose_name = "Epizod"
        verbose_name_plural = "Epizodlar"
        ordering = ["episode_number"]


class Coments(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name="Anime")
    name = models.CharField(max_length=100, verbose_name="Isim")
    text = models.TextField(max_length=1000, verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Komentariya"
        verbose_name_plural = "Komentariyalar"