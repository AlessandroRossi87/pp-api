from django.urls import path
from .views import ReactionList, ReactionDetail

urlpatterns = [
    path('reactions/', ReactionList.as_view()),
    path('reactions/<int:pk>/', ReactionDetail.as_view()),
]