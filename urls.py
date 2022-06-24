from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import *

from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, PostSitemap, staffUnitSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'posts': PostSitemap,
    'staff': staffUnitSitemap,
    }

urlpatterns = [
    path('', index, name='home'),
    path('kontaktyi/', contactView, name='contact'),
    path('agreement/', agreementView, name='agreement'),
    path('legal-confidential/', legalView, name='legal'),
    path('reception-director/<slug:staff_slug>/', show_staff_item, name='staff'),
    path('reception-director/', directorView.as_view(), name='reception_director'), #Все сотрудники
    path('uslugi/', priceView, name='price'),
    path('license/', licenseView, name='license'),
    path('news-and-articles-about-cosmetology/', ArticlesView.as_view(), name='articles'), #статьи
    path('directions-of-cosmetology/<slug:dir_cat_slug>/<slug:dir_slug>/', Get_Direction_Item.as_view(), name='direction'), # Направления косметологии
    #path('directions-of-cosmetology/<slug:dir_cat_slug>/<slug:dir_slug>/', Show_Direction_Item, name='direction'),  # Направления косметологии
    path('directions-of-cosmetology/<slug:dir_cat_slug>/', cosmetology_by_sections.as_view(), name='directions_of_cosmetology'), # Разделы направлений
    path('directions-of-cosmetology/', directions_of_cosmetology.as_view(), name='directions_of_cosmetology'), #Все разделы направлений
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    ]
