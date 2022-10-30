from django.db import models

class HomePage(models.Model):
    news = models.TextField(blank=True)
    work_schedule = models.TextField(blank=True)
    
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    working_position = models.ForeignKey('Working_professions', on_delete=models.PROTECT, null=True)
    phone = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.working_position
    
class Working_professions(models.Model):
    profession = models.CharField(max_length=50)
    
    def __str__(self):
        return self.profession
    