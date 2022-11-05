from django.db import models
from django.urls import reverse


class HomePage(models.Model):
    news = models.TextField(blank=True, verbose_name='Новости')
    work_schedule = models.TextField(blank=True,
                                     verbose_name='Расписание работы')
    week_number = models.IntegerField(default=0, verbose_name='Номер недели')
    
    def __str__(self):
        return self.news
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'week_number': self.week_number})

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'
        ordering = ['-week_number']
