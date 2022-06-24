from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

# Create your views here.
from blog.forms import *

#Вывод всех категорий
class directions_of_cosmetology(ListView):
    model = directionCategory
    template_name = 'blog/directions.html'
    context_object_name = 'dir_category'  # вместо object_list
    allow_empty = False
    extra_context = {
        'title': 'Направления косметологии',
        'description': 'Направления косметологии в Ярославле. Подробнее в разделе сайта ...',
        'WorkingHours': WorkingHours,
        'social': social,
        'menu': menu,
    }

    def get_queryset(self):
        return directionCategory.objects.all()



# Вывод всех статей категории для двух slugs
class cosmetology_by_sections(ListView):
    model = directionCosmet
    template_name = 'blog/by_sections.html'
    context_object_name = 'cosmets'  # вместо object_list
    allow_empty = False
    extra_context = {
        'WorkingHours': WorkingHours,
        'social': social,
        'menu': menu,
    }

    def get_queryset(self):
        return directionCosmet.objects.filter(is_published=True, dir_category__slug=self.kwargs['dir_cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = directionCategory.objects.get(slug=self.kwargs['dir_cat_slug'])
        return context

#Вывод одной статьи по двум slugs
class Get_Direction_Item(DetailView):
        model = directionCosmet
        template_name = 'blog/direction_item.html'
        context_object_name = 'direction_item'
        allow_empty = False
        extra_context = {
            'WorkingHours': WorkingHours,
            'social': social,
            'menu': menu,
        }

        def get_object(self, *args, **kwargs):
            return directionCosmet.objects.get(slug=self.kwargs.get('dir_slug'),
                                           dir_category__slug=self.kwargs.get('dir_cat_slug'))


        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = directionCategory.objects.get(slug=self.kwargs['dir_cat_slug'])
            context['dir_slug'] = directionCategory.objects.values().get(slug=self.kwargs['dir_cat_slug'])['slug']
            return context


          
