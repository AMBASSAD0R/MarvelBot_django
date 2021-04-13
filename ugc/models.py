from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
    )
    name = models.TextField(
        verbose_name='Имя пользователя',
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
