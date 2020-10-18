from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound

from vacancies.models import Company, Specialty, Vacancy


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()

        return render(request, 'index.html', context={'specialties': specialties,
                                                      'companies': companies})


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        all_count = len(vacancies)

        return render(request, 'vacancies.html', context={'vacancies': vacancies,
                                                          'all_count': all_count})


class CategoryVacanciesView(View):
    def get(self, request, code):
        if not Specialty.objects.filter(code=code).exists():
            return HttpResponseNotFound('specialty not found')
        vacancies = Vacancy.objects.filter(specialty__code=code)
        count = len(vacancies)
        title = Specialty.objects.get(code=code).title

        return render(request, 'category_vacancies.html', context={'title': title,
                                                                   'vacancies': vacancies,
                                                                   'count': count})


class CompanyView(View):
    def get(self, request, company_id):
        if not Company.objects.filter(id=company_id).exists():
            return HttpResponseNotFound('company not found')
        vacancies = Vacancy.objects.filter(company__id=company_id)
        count = len(vacancies)
        company = Company.objects.get(id=company_id)

        return render(request, 'company.html', context={'vacancies': vacancies,
                                                        'count': count,
                                                        'company': company})


class VacancyView(View):
    def get(self, request, vacancy_id):
        if not Vacancy.objects.filter(id=vacancy_id).exists():
            return HttpResponseNotFound('vacancy not found')
        vacancy = Vacancy.objects.get(id=vacancy_id)

        return render(request, 'vacancy.html', context={'vacancy': vacancy})
