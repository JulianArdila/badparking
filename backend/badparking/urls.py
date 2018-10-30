from django.conf.urls import url
from badparking import views

urlpatterns = [
    url(r'^tipo usuarios/$', views.TipoUsuarioList.as_view()),
    url(r'^tipo usuarios/(?P<pk>[0-9]+)/$', views.TipoUsuarioDetail.as_view()),
    url(r'^usuarios/$', views.UsuariosList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuariosDetail.as_view()),
    url(r'^registros mal parquedos/$', views.IngreMalParqueadoList.as_view()),
    url(r'^registros mal parquedos/(?P<pk>[0-9]+)/$', views.IngreMalParqueadoDetail.as_view()),
    url(r'^calificacion/$', views.CalificacionList.as_view()),
    url(r'^calificacion/(?P<pk>[0-9]+)/$', views.CalificacionDetail.as_view()),
]