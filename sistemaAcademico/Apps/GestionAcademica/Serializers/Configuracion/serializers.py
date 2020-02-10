from rest_framework import serializers
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_conf import *
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import GenrGeneral


class moduloSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConfModulo
        fields = ['id_modulo','codigo','nombre']
        

class menuSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConfMenu
        fields = "__all__"



class moduloSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConfModulo
        fields = ['id_modulo','codigo','nombre']

class empresaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConfEmpresa
        fields = ['id_empresa','nombre','razon_social']
