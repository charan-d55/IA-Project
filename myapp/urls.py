from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/<int:year>/<int:month>/', views.about, name='about'),
    path('greet/', views.GreetView.as_view(), name='greet'),  # Updated path for CBV
    path('<int:type_no>/', views.detail, name='detail'),
]