from django.db import models
from django.urls import reverse


class Employee(models.Model):
    full_name = models.CharField(max_length=150,
                                 unique=True,
                                 verbose_name='Имя')
    working_profession = models.ForeignKey('Working_professions',
                                            on_delete=models.PROTECT,
                                            null=True,
                                            verbose_name='Прфессия')
    phone = models.CharField(max_length=50, blank=True,
                             verbose_name='Номер телефона')
    
    def __str__(self):
        return self.full_name + " " + self.working_position
    
    def get_absolute_url(self):
        return reverse('employee', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['full_name']


class Working_professions(models.Model):
    profession = models.CharField(max_length=50,
                                  unique=True,
                                  verbose_name='Прфессия')
    
    def __str__(self):
        return self.profession
    
    def get_absolute_url(self):
        return reverse('working_profession', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Прфессия'
        verbose_name_plural = 'Прфессии'
        ordering = ['profession']


class Technological_operation(models.Model):
    name_operations = models.CharField(max_length=50,
                                       unique=True,
                                       verbose_name='Технологическая '
                                                    'операция')
    working_profession = models.ForeignKey('Working_professions',
                                         on_delete=models.PROTECT, null=True,
                                         verbose_name='Прфессия')
    
    def __str__(self):
        return self.name_operations
    
    def get_absolute_url(self):
        return reverse('technological_operation', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Технологическая операция'
        verbose_name_plural = 'Технологические операции'
        ordering = ['name_operations']
        
class Work_task(models.Model):
    name_operations = models.ForeignKey(
        Technological_operation, to_field='name_operations',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Прфессия')
    full_name = models.ForeignKey(Employee, to_field='full_name',
                                  on_delete=models.PROTECT,
                                  null=True,
                                  verbose_name='ФИО')
    time_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата добавления')
    is_done = models.BooleanField(default=False, verbose_name='Готовность')
    work_time = models.FloatField(default=0,
                                  verbose_name='Время выполнения',
                                  blank=True)
    notes = models.TextField(blank=True, verbose_name='Примечание')
    
    def __str__(self):
        return self.name_operations
    
    def get_absolute_url(self):
        return reverse('work_task', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Рабочее задание'
        verbose_name_plural = 'Рабочие задания'
        ordering = ['name_operations']
