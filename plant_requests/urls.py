from django.urls import path
from .views import NewPlantRequest, ApprovePlantRequest, DenyPlantRequest,


urlpatterns = [
    path('plants/<int:plant_id>/request/', NewPlantRequest.as_view(), name='new-request'),
    path('plant-requests/<int:pk>/approve/', ApprovePlantRequest.as_view(), name='approve-request'),
    path('plant-requests/<int:pk>/deny/', DenyPlantRequest.as_view(), name='deny-request'),
]