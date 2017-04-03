from django.shortcuts import render, redirect
from .models import Ano, Escala, Analista
from datetime import datetime, date


def index(request):
    user_logado = Analista.objects.get(pk=1)
    data_atual = datetime.today()
    ano = str(data_atual.year)
    mes = str(data_atual.month)
    analistas_por_escala = Escala.objects.filter(ano__ano=ano).filter(mes=mes)

    year = int(ano)
    month = int(mes)
    tabela_header = {}

    try:
        for x in range(1, 32):
            dia_semana_number = date(year, month, x).isoweekday()
            if dia_semana_number == 1:
                dia_semana = 'Seg'
            elif dia_semana_number == 2:
                dia_semana = 'Ter'
            elif dia_semana_number == 3:
                dia_semana = 'Qua'
            elif dia_semana_number == 4:
                dia_semana = 'Qui'
            elif dia_semana_number == 5:
                dia_semana = 'Sex'
            elif dia_semana_number == 6:
                dia_semana = 'Sab'
            elif dia_semana_number == 7:
                dia_semana = 'Dom'

            tabela_header.update({x: dia_semana})
    except:
        pass

    total_de_dias = len(tabela_header)

    anos_do_menu = Ano.objects.all()
    return render(request, 'tabela_escala/index.html', {'analistas_por_escala': analistas_por_escala,
                                                        'anos_do_menu': anos_do_menu, 'tabela_header': tabela_header,
                                                        'total_de_dias': total_de_dias,
                                                        'user_logado': user_logado,
                                                        })

def escala_ano_mes(request, ano, mes):

    user_logado = Analista.objects.get(pk=1)
    analistas_por_escala = Escala.objects.filter(ano__ano=ano).filter(mes=mes)
    anos_do_menu = Ano.objects.all()
    title = datetime(int(ano), int(mes), 1).strftime("%B, %Y")

    year = int(ano)
    month = int(mes)
    tabela_header = {}
    try:
        for x in range(1, 32):
            dia_semana_number = date(year, month, x).isoweekday()
            if dia_semana_number == 1:
                dia_semana = 'Seg'
            elif dia_semana_number == 2:
                dia_semana = 'Ter'
            elif dia_semana_number == 3:
                dia_semana = 'Qua'
            elif dia_semana_number == 4:
                dia_semana = 'Qui'
            elif dia_semana_number == 5:
                dia_semana = 'Sex'
            elif dia_semana_number == 6:
                dia_semana = 'Sab'
            elif dia_semana_number == 7:
                dia_semana = 'Dom'
            tabela_header.update({x: dia_semana})
    except:
        pass
    total_de_dias = len(tabela_header)

    return render(request, 'tabela_escala/escalas.html', {'analistas_por_escala': analistas_por_escala,
                                                          'anos_do_menu': anos_do_menu,
                                                          'title': title,
                                                          'tabela_header': tabela_header,
                                                          'total_de_dias': total_de_dias,
                                                          'user_logado': user_logado,
                                                          'ano': ano,
                                                          'mes': mes,
                                                          })

def editar(request, ano, mes):
    user_logado = Analista.objects.get(pk=1)
    analistas_por_escala = Escala.objects.filter(ano__ano=ano).filter(mes=mes)
    anos_do_menu = Ano.objects.all()
    title = datetime(int(ano), int(mes), 1).strftime("%B, %Y")

    escala = Escala()
    lista_expediente = escala.get_lista_turnos()

    year = int(ano)
    month = int(mes)
    tabela_header = {}
    try:
        for x in range(1, 32):
            dia_semana_number = date(year, month, x).isoweekday()
            if dia_semana_number == 1:
                dia_semana = 'Seg'
            elif dia_semana_number == 2:
                dia_semana = 'Ter'
            elif dia_semana_number == 3:
                dia_semana = 'Qua'
            elif dia_semana_number == 4:
                dia_semana = 'Qui'
            elif dia_semana_number == 5:
                dia_semana = 'Sex'
            elif dia_semana_number == 6:
                dia_semana = 'Sab'
            elif dia_semana_number == 7:
                dia_semana = 'Dom'
            tabela_header.update({x: dia_semana})
    except:
        pass
    total_de_dias = len(tabela_header)



    return render(request, 'tabela_escala/editar.html', {'analistas_por_escala': analistas_por_escala,
                                                         'anos_do_menu': anos_do_menu,
                                                         'title': title,
                                                         'tabela_header': tabela_header,
                                                         'total_de_dias': total_de_dias,
                                                         'user_logado': user_logado,
                                                         'lista_expediente' : lista_expediente,                                                                                                                   'ano': ano,
                                                         'mes': mes,
                                                         'ano': ano,
                                                         })

def confirma_edicao(request, ano, mes):
    analistas_por_escala = Escala.objects.filter(ano__ano=ano).filter(mes=mes)

    return redirect(escala_ano_mes, ano=ano, mes=mes)
