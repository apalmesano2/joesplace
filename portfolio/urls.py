from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^catering/$', views.catering, name='catering'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^events/$', views.events, name='events'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^specials/$', views.specials, name='specials'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]
