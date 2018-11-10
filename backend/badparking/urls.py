from django.conf.urls import url
from badparking import views

urlpatterns = [
    url(r'^tipoUsuarios/$', views.TipoUsuarioList.as_view()),
    url(r'^tipoUsuarios/(?P<pk>[0-9]+)/$', views.TipoUsuarioDetail.as_view()),
    url(r'^usuarios/$', views.UsuariosList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuariosDetail.as_view()),
    url(r'^registrosMalParquedos/$', views.IngreMalParqueadoList.as_view()),
    url(r'^registrosMalParquedos/(?P<pk>[0-9]+)/$', views.IngreMalParqueadoDetail.as_view()),
    url(r'^calificacion/$', views.CalificacionList.as_view()),
    url(r'^calificacion/(?P<pk>[0-9]+)/$', views.CalificacionDetail.as_view()),
]