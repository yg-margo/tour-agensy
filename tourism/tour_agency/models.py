from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.postgres import fields


class Country(models.Model):
    country_name = models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class FoodType(models.Model):
    type = models.CharField(max_length=100, verbose_name="Тип питания")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип питания"
        verbose_name_plural = "Типы питания"


class Tour(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название тура')
    country = models.ManyToManyField(Country, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    available_dates = fields.ArrayField(models.DateField(),
                                        verbose_name='Доступные даты',
                                        default=list)
    duration = models.IntegerField(verbose_name='Продолжительность')
    tour_agency = models.CharField(max_length=100, verbose_name="Турагенство")

    food_type = models.ManyToManyField(FoodType, verbose_name="Тип питания")
    hotel_category = fields.ArrayField(
        models.IntegerField(validators=[MinValueValidator(1),
                                        MaxValueValidator(5)]),
        verbose_name='Категория отеля', default=list)
    description = models.CharField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Tourist(AbstractUser):
    tours = models.ManyToManyField(Tour, through='TourBooking',
                                   verbose_name='Туры',
                                   related_name='tourists', blank=True)


class TourBooking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE,
                             verbose_name='Тур')
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE,
                                verbose_name='Турист')
    selected_date = models.DateField(verbose_name='Выбранная дата')
    selected_category = models.IntegerField(verbose_name='Категория отеля',
                                            validators=[MinValueValidator(1),
                                                        MaxValueValidator(5)])
    persons_number = models.IntegerField(verbose_name='Количество взрослых')
    children_number = models.IntegerField(verbose_name='Количество детей')
    rooms_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Количество номеров')

    STATUSES = (
        ('W', "Ожидает подтверждения"),
        ('B', 'Забронирован'),
        ('C', 'Отказано'),
        ('D', 'Завершен')
    )
    status = models.CharField(choices=STATUSES, max_length=100,
                              verbose_name='Статус бронирования')

    def __str__(self):
        return self.tour.name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE,
                             verbose_name='Тур')
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE,
                                verbose_name='Турист')
    text = models.CharField(max_length=1000, verbose_name='Текст отзыва')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)],
                                 verbose_name='Оценка')
    booking = models.ForeignKey(TourBooking, on_delete=models.CASCADE,
                                verbose_name="Бронирование")

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
