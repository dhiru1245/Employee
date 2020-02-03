from django.db import models
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=80)
    pan_no = models.CharField(max_length= 8, unique=True, null=True)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=50, unique=True, null=True)
    city_name = models.CharField(max_length=80)

    def __str__(self):
        return self.ename

    # def get_absolute_url(self):
    #     return reverse('emp_edit', kwargs={'pk': self.pk})