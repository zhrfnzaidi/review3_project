from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="index"),
    path('u_review', views.u_review, name="u_review"),
]

urlpatterns += staticfiles_urlpatterns()