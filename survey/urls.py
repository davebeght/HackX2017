from django.conf.urls import url, include


from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^registration/', views.registration, name="registration")
]
