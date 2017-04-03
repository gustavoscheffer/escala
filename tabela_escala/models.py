from __future__ import unicode_literals

from django.db import models


class Analista(models.Model):

    nome = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)

    def __str__(self):
        return (self.nome)


class Ano(models.Model):

    ano = models.PositiveIntegerField(null=False)

    def __str__(self):
        # Atention -> this field is int but is't necesary convert to str on return
        return str(self.ano)


class Escala(models.Model):

    MES_OPCOES = (
        ('1', 'Janeiro'),
        ('2', 'Fevereiro'),
        ('3', 'Marco'),
        ('4', 'Abril'),
        ('5', 'Maio'),
        ('6', 'Junho'),
        ('7', 'Julho'),
        ('8', 'Agosto'),
        ('9', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro'),
    )
    TURNO_OPCOES = (
        ('07-16', '07-16'),
        ('08-17', '08-17'),
        ('09-18', '09-18'),
        ('10-19', '10-19'),
        ('11-20', '11-20'),
        ('12-21', '12-21'),
        ('13-22', '13-22'),
        ('14-23', '14-23'),
        ('22-07', '22-07'),
        ('Folga', 'Folga'),
        ('Ferias', 'Ferias'),
        ('Atestado', 'Atestado'),
        ('Indisponivel', 'Indisponivel'),
    )

    mes = models.CharField(max_length=2, choices=MES_OPCOES)
    ano = models.ForeignKey('Ano', related_name='anos')
    analista = models.ForeignKey('Analista', related_name='analistas')
    dia_1 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_2 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_3 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_4 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_5 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_6 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_7 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_8 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_9 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_10 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_11 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_12 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_13 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_14 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_15 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_16 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_17 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_18 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_19 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_20 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_21 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_22 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_23 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_24 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_25 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_26 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_27 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_28 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_29 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_30 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)
    dia_31 = models.CharField(max_length=15, default='Indisponivel', choices=TURNO_OPCOES)

    def get_lista_turnos(self):
        return self.TURNO_OPCOES

    def __str__(self):
        return self.analista.nome
