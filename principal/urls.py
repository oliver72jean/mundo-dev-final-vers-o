from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('pub1', views.pub1, name='pub1'),
    path('pub2', views.pub2, name='pub2'),
    path('pub3', views.pub3, name='pub3'),
    path('pub4', views.pub4, name='pub4'),
    path('pub5', views.pub5, name='pub5'),
    path('pub6', views.pub6, name='pub6'),
    path('pub7', views.pub7, name='pub7'),
    path('pub8', views.pub8, name='pub8'),
    path('pub9', views.pub9, name='pub9'),
    path('pub10', views.pub10, name='pub10')
]
