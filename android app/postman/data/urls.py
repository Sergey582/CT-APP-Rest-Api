from django.urls import path
from .views import TestView

app_name = "data"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('test/', TestView.as_view()),
    path('test/<int:pk>', TestView.as_view()),

    

]
