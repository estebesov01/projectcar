from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin = models.CharField('ВИН', db_index=True, unique=True, max_length=20)
    color = models.CharField('Цвет машины', max_length=20)
    brand = models.CharField('Марка машины', max_length=20)
    CAR_TYPE = (
        (1, 'Седан'),
        (2, 'Хетчбек'),
        (3, 'Универсал'),
        (4, 'Внедорожник'),
        (5, 'Спортивный'),
    )
    car_type = models.IntegerField('Тип машины', choices=CAR_TYPE, default='Выберите машину')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


