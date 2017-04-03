from django.contrib import admin
from . models import Analista, Ano, Escala

# Register your models here.
# admin.site.register(Analista)


@admin.register(Analista)
class AnalistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')
    list_filter = ('id', 'nome', 'email')
    search_fields = ['id', 'nome', 'email']


@admin.register(Ano)
class AnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ano',)
    list_display_links = ('id', 'ano',)
    list_filter = ('id', 'ano',)
    search_fields = ['id', 'ano']


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'analista', 'mes', 'ano')
    list_display_links = ('id', 'analista', 'mes', 'ano')
    list_filter = ('id', 'analista', 'mes', 'ano')
    search_fields = ['mes', 'analista__nome', 'ano__ano']
    save_as = True
