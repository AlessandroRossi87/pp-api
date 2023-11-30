from django.urls import path
from plants import views

urlpatterns = [
    path('plants/', views.PlantList.as_view()),
    path('plants/<int:pk>/', views.PlantDetail.as_view()),
    path('api/taxonomy-choices/', views.TaxonomyChoices.as_view(), name='taxonomy-choices'),
]