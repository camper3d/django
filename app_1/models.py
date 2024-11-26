from django.db import models

class Mebel(models.Model):
    link = models.TextField('Cсылка')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(
        # 'Описание',
        verbose_name='описание с куфара'
    )
    parse_datetime = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name= 'дата прихода к нам'
    )

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f'{self.price} | {self.description[:60]}'

    class Meta:
        verbose_name = 'мебель'
        verbose_name_plural = 'мебель'
        ordering = ['parse_datetime', 'price']
