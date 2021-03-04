from django.urls import path
from .views import home, add, update, delete, edit
urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('edit/<int:pk>', edit, name='edit'),
]