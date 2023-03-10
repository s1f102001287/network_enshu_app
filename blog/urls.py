from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:article_id>/update', views.update, name='update'),
	path('<int:article_id>/delete', views.delete, name='delete'),
	path('<int:article_id>/', views.detail, name='detail'),
]