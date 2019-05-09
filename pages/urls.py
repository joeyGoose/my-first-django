from django.urls import path

from .views import home, visitors

urlpatterns = [
    path('', home, name='home_page'),
    path('visitors', visitors, name='visitors_page')
]