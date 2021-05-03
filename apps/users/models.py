from django.db import models

class User(models.Model):
    first_name = models.CharField(max_lenght=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.last_name.capitalize()} {self.first_name.capitalize()}'

