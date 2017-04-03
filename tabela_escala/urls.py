from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ano>[0-9]{4})/(?P<mes>[0-9]+)$', views.escala_ano_mes, name='ano_mes'),
    url(r'^(?P<ano>[0-9]{4})/(?P<mes>[0-9]+)/editar$', views.editar, name='editar'),
    url(r'^(?P<ano>[0-9]{4})/(?P<mes>[0-9]+)/confirmar$', views.confirma_edicao, name='confirmar'),
]
