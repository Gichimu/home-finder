from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name = 'home'),
    url(r'^api/properties$', views.proList.as_view()),
    url(r'^save', views.save, name = 'save'),
    url(r'api/properties/property-id/(?P<pk>[0-9]+)$', views.proDescription.as_view())
]