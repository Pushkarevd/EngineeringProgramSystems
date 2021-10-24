import numpy as np
from django.shortcuts import render, redirect
from django.views import View

from .models import Form
from .create_plots import queryset_to_img
from .prediction import predict


class MainView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        author = request.user
        uni_course = request.POST.get('uni_course')
        soft_course = request.POST.get('soft_course')
        online_course = request.POST.get('online_course')
        difficulty_of_courses = request.POST.get('difficulty_of_courses')
        hardest_teacher = request.POST.get('hardest_teacher').upper()
        self_opinion = request.POST.get('self_opinion')
        try:
            Form.objects.get(author=author).delete()
        except:
            pass
        Form.objects.create(author=author,
                            uni_course=uni_course,
                            soft_course=soft_course,
                            online_course=online_course,
                            difficulty_of_courses=difficulty_of_courses,
                            hardest_teacher=hardest_teacher,
                            self_opinion=self_opinion)
        return redirect('/analytic')


class AnalyticPage(View):
    def get(self, request):
        all_objects = Form.objects.all()

        uni_plot = queryset_to_img(all_objects,
                                   'uni_course',
                                   'Качество обучения')

        soft_plot = queryset_to_img(all_objects,
                                    'soft_course',
                                    'Уровень удовлетворенности soft skill')

        online_plot = queryset_to_img(all_objects,
                                      'online_course',
                                      'Уровень удовлетворенности онлайн курсами')

        difficulty_plot = queryset_to_img(all_objects,
                                          'difficulty_of_courses',
                                          'Предметная сложность по мнению пользователей')

        hardest_plot = queryset_to_img(all_objects,
                                       'hardest_teacher',
                                       'Самый сложный преподаватель')
        count_forms = Form.objects.count()
        return render(request, 'analytic.html', {'uni_plot': uni_plot,
                                                 'soft_plot': soft_plot,
                                                 'online_plot': online_plot,
                                                 'difficulty_plot': difficulty_plot,
                                                 'hardest_plot': hardest_plot,
                                                 'counter': count_forms})

class ForecastPage(View):
    def get(self, request):
        all_objects = Form.objects.all().values()

        keys = [
            'uni_course',
            'soft_course',
            'online_course',
            'difficulty_of_courses'
        ]
        form_names = [
            'Качество обучения',
            'Уровень удовлетворенности soft skill',
            'Уровень удовлетворенности онлайн курсами',
            'Предметная сложность по мнению пользователей'
        ]
        predictions = {
            form_names[i]: round(np.mean(predict(all_objects, keys[i])), 2) for i in range(len(form_names))
        }
        print(predictions)
        return render(request, 'forecast.html', {'predictions': predictions})