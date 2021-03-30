from django.urls import path
from . import views
from .views import Pdf

urlpatterns = [
    path('post/', views.add_ques,name='post'),
    path('list/',views.ques_list,name='list'),
    path('pdf/', Pdf.as_view(),name='pdf')

]
