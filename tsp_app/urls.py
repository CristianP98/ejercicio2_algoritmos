from django.urls import path
from . import views

urlpatterns = [
    path('', views.tsp_view, name='tsp_view'),
    path('compare/', views.compare_results_view, name='compare_results_view'),
    # Otras URLs
]