from . import views
from django.urls import path

urlpatterns = [
    path('new/',views.CreateNewHomework.as_view(),name='create_new_homework_page'),
    path('edit/<int:postid>/',views.EditHomework.as_view(),name='edit_homeowork_page'),
]
