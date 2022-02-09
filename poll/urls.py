from django.urls import path
from . import views


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:question_id>', views.detail.as_view(), name='detail'),
    path('<int:question_id>/results/', views.results.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote.as_view(), name='vote'),
    path('create', views.create.as_view(), name='create'),
    path('save', views.save.as_view(), name='save'),
    path('<int:question_id>/options/', views.options.as_view(), name='options'),
    path('<int:question_id>/choice/', views.choice.as_view(), name='choice'),       
]
