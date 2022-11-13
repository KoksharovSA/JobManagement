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
        return reverse('post', kwargs={'number_week': self.week_number})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-week_number']
