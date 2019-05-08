from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url('signup/', views.signup, name='signup'),
	url('login/', views.login, name='login')
	]