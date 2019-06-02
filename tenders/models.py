from django.db import models


class Tender(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateField()

    def __str__(self):
        return f'#{self.number} ({self.description})'
