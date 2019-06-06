from django.db import models


class Tender(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateField()

    def __str__(self):
        return f'#{self.number} ({self.description})'


class KeyWord(models.Model):
    category = models.CharField(max_length=150, verbose_name='Название категории')
    plus_keywords = models.TextField(verbose_name='Плюс-слова')
    minus_keywords = models.TextField(verbose_name='Минус-слова')

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

