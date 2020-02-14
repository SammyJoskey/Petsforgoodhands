from django.db import models
from django.urls import reverse
from slugify import slugify


class Pet(models.Model):
    cat = 'c'
    dog = 'd'
    parrot = 'p'
    SPECIES_CHOICES = (
    ('p', 'Попугай'),
    ('c', 'Кошка'),
    ('d', 'Собака'),
    )
    spec = models.CharField(
        max_length=10,
        choices=SPECIES_CHOICES,
        blank=True,
        verbose_name='Вид животного'
    )
    male = 'm'
    female = 'f'
    SEX_CHOICES = (
    ('m', 'Мальчик'),
    ('f', 'Девочка'),
    )
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES,
        blank=True,
        verbose_name='Пол'
    )
    age = models.CharField (max_length=20, verbose_name='Возраст')   
    name = models.CharField (max_length=20, verbose_name='Кличка')  
    breed = models.CharField (max_length=50, verbose_name='Порода')  
    description = models.TextField (blank=True, verbose_name='Описание')  
    arrival_date = models.DateTimeField (auto_now_add=True, db_index=True, verbose_name='Дата добавления')
    image = models.ImageField (upload_to='img/%Y/%m/%d', verbose_name='Фото')
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name

    # транслитерируем кличку для добавления в url
    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Pet, self).save(*args, **kwargs)
    
    class Meta():
        verbose_name='Животное'
        verbose_name_plural='Животные'
    
    def get_absolute_url(self):
        return reverse("pets_detail", kwargs={'slug': self.slug})

    
class News(models.Model):
    title = models.CharField (max_length=200, verbose_name='Новость')
    text = models.TextField (verbose_name='Текст')
    pub_date = models.DateTimeField (auto_now_add=True, db_index=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name='Новость'
        verbose_name_plural='Новости'