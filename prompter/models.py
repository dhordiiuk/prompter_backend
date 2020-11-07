from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Mode(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    description = models.TextField(blank=True)
    min_time_sec = models.IntegerField(default=5)
    max_time_sec = models.IntegerField(default=10)

    class Meta:
        ordering = ('name',)
        verbose_name = 'mode'
        verbose_name_plural = 'modes'

    def __str__(self):
        return self.name


class Word(models.Model):
    mode = models.ForeignKey(Mode, related_name='words', on_delete=models.CASCADE)
    name = models.CharField(max_length=120, db_index=True)
    importance = models.IntegerField(default=5,
                                    validators=[
                                        MaxValueValidator(10),
                                        MinValueValidator(0)
                                    ])
    use = models.BooleanField(default=True)

    class Meta:
        unique_together = ('mode', 'name', 'importance', 'use')

    def __str__(self):
        return self.name
