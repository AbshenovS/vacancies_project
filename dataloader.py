import os
import django
from datetime import datetime
from random import randint

import data

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from vacancies.models import Company, Specialty, Vacancy

if __name__ == '__main__':
    Vacancy.objects.all().delete()
    Specialty.objects.all().delete()
    Company.objects.all().delete()

    for company in data.companies:
        Company.objects.create(
            name=company['title'],
            location='Москва и удаленно',
            logo='https://place-hold.it/100x60',
            description='Мы крутая команда',
            employee_count=randint(5, 50)
        )

    for specialty in data.specialties:
        Specialty.objects.create(
            title=specialty['title'],
            code=specialty['code'],
            picture='https://place-hold.it/100x60'
        )

    for job in data.jobs:
        specialty = Specialty.objects.get(code=job['cat'])
        company = Company.objects.get(name=job['company'])
        Vacancy.objects.create(
            title=job['title'],
            description=job['desc'],
            salary_min=int(job['salary_from']),
            salary_max=int(job['salary_to']),
            published_at=datetime.strptime(job['posted'], '%Y-%m-%d'),
            specialty=specialty,
            company=company)
