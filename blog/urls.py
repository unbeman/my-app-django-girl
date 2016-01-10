from django.cong.urls import url
from . import views

utlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]