from django.urls import path

from . import views

urlpatterns = [
    path('', views.studentHome, name='studentHome'),
    path('m_home/', views.mentorHome, name='mentorHome'),
    path('m_home/details/<int:id>', views.requestDetails, name='requestDetails'),
    path('ajax/sec_req', views.section_request, name = "sec_req"),
    path('ajax/requested_section', views.requested_section, name = "req_sec"),
    path('ajax/handleApproval', views.handleRequestApproval, name = "handleRequestApproval"),
    path('ajax/handleComment', views.handleComment, name = "handleComment"),
]