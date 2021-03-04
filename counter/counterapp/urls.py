from django.urls import path
from .views import home, increment, decrement, reset
urlpatterns = [
    path('', home, name='home'),
    path('increment', increment, name='increment'),
    path('decrement', decrement, name='decrement'),
    path('reset', reset, name='reset')
]
