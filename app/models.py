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
    




from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=255, verbose_name="Kategoriya slug")

    def __str__(self):
        return self.name

from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200, verbose_name="Anime Sarlavhasi")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Tavsif")
    category = models.ManyToManyField('Category', verbose_name="Kategoriya")
    release_date = models.DateField(verbose_name="Chiqarilish Sanasi")
    episode_count = models.IntegerField(verbose_name="Epizodlar Soni")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar Soni")
    coments_count = models.IntegerField(default=0, verbose_name="Izohlar Soni")
    cover_image = models.ImageField(upload_to='covers/', verbose_name="Qopqoq Rasm")
    header_image = models.ImageField(upload_to='headers/', verbose_name="Header Rasm", default="https://coffective.com/wp-content/uploads/2018/06/default-featured-image.png.jpg")
    header_publish = models.BooleanField(default=False, verbose_name="Headerni Chop Etish")

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
        