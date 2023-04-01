from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentHome, name='studentHome'),
    path('ajax/sec_req', views.section_request, name = "sec_req"),
]