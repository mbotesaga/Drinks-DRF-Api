from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)
