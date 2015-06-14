from django.conf.urls import patterns, include, url
from django.contrib import admin
from crm import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
    url(r'^crm/', include('crm.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^add_individual/', views.add_individual, name='add_individual'),
)