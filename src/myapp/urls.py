from django.urls import path
from . import views

urlpatterns = [
    #Auth
    path("register", views.sign_up, name="sign_up"),
    
    path("index", views.index, name="index"),
    path("education", views.education, name='education'),
    path("work-history", views.work_history, name='work_history'),
    path("skill", views.skills, name = 'skills'),
    path("others", views.others, name="others"),
    
    path('generate-pdf', views.generate_pdf, name='generate_pdf'),
]
