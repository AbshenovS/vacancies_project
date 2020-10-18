from django.db import models


class Company(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    objects = models.Manager()
    code = models.CharField(max_length=1000)
    title = models.CharField(max_length=64)
    picture = models.CharField(max_length=1000)


class Vacancy(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=64, default='no skills required')
    description = models.CharField(max_length=1000)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
