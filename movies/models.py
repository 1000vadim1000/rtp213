from django.db import models

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Razrabs(models.Model):
    name = models.CharField("Имя", max_length=180)
    description = models.TextField("Описание", default=0)
    image = models.ImageField("Изображение" upload_to="actors/")



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Разработчики и компания"
        verbose_name_plural = "Разработчики и компания"





class Genre(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"




class Movie(models.Model):
    title = models.CharField("Название", max_length=100)
    taglime = models.CharField("Слоган", max_length=100, default="")
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveIntegerField("Дата выхода", default=2021)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="Режиссёр" related_name="film_director")
    actors =  models.ManyToManyField()



