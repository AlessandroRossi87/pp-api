from django.urls import path
from .views import NewPlantRequest, ApprovePlantRequest


urlpatterns = [
    path('plants/<int:plant_id>/request/', NewPlantRequest.as_view(), name='new-request'),
    path('plant-requests/<int:pk>/approve/', ApprovePlantRequest.as_view(), name='approve-request'),
]