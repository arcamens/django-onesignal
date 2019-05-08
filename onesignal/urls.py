from django.views.generic.base import RedirectView
from django.conf.urls import url
from . import views

app_name = 'onesignal'
urlpatterns = [
    url(r'^update-uuid/', views.UpdateUuid.as_view(),  name='update-uuid'),

]






