from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('newproject/',views.addProject,name = 'add_project'),
    path('projects/<id>/',views.projects,name = 'projects'),
   path('ratings/', include('star_ratings.urls', namespace='ratings')),
   path('rate/<id>/',views.rate,name = 'rate')
]