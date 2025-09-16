from django.urls import path
from . import views


urlpatterns = [
    path('polls/', views.PollListCreate.as_view(), name='poll-list-create'),
    path('polls/<int:pk>/', views.PollDetail.as_view(), name='poll-detail'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', views.VoteCreate.as_view(), name='choice-vote'),
]