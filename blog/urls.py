from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('hobbies', views.hobbies, name='hobbies'),
    path('hobbies/<int:id>', views.hobby_detail, name='hobby_detail'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/<int:id>', views.portfolio_detail, name='portfolio_detail'),
    path('contact', views.contact, name='contact'),
]
