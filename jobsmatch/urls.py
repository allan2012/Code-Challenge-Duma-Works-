from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    
    url(r'^verify/$', views.verify, name='verify'),
    
    url(r'^logout$', views.log_out, name='log_out'),
    
    url(r'^applicant/(?P<user_id>[0-9]+)$', views.applicant, name='applicant'),

    url(r'^profile$', views.profile, name='profile'),
    
    url(r'^admin$', views.admin, name='admin'),
    
    url(r'^register$', views.register, name='register'),
    
    url(r'^add_job/$', views.add_job, name='add_job'),
    
    url(r'^criteria/$', views.criteria, name='criteria'),
    
    url(r'^filter_job/$', views.filter_job, name='filter_job'),
    
]