from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_conf import *
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import *
from sistemaAcademico.Apps.GestionAcademica.Serializers.Configuracion.serializers import *
import socket
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.db.models import Q

class Menu_api(APIView): 

    def post(self, request):
        if self.request.data is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            descripcion = self.request.data['descripcion']
            url = self.request.data['url']
            lazyname = self.request.data['lazyname']
            view = self.request.data['view']
            name = self.request.data['name']
            try:
                
                queryset = ConfMenu.objects.filter(
                    Q(descripcion__contains=descripcion)
                    & Q(url=url)#or
                    & Q(view=view)#or
                    & Q(lazy_name=lazyname)#or
                    & Q(name=name)#or
                    & Q(id_genr_estado=97)#and
                )

                if queryset:  
                    serializacion = menuSerializers(queryset, many=True)
                    return Response(data=serializacion.data, status=status.HTTP_226_IM_USED)

                else:
                    serializacion = menuSerializers(queryset, many=True)
                    return Response(data=serializacion.data, status=status.HTTP_200_OK)

            except Exception as e:
                print(e)


class Unidad_Edu(APIView):

    def post(self, request):
        if self.request.data is None:
            return Response(status=status.HTTP_204_NO_CONTENT)#Mensaje_existoso_pero no devuelve_nada

        else:
            nombre = self.request.data['nombre']
            razon_social = self.request.data['razon_social']
            correo = self.request.data['correo']
            identificacion = self.request.data[' identificacion']
            try:
                queryset = ConfEmpresa.objects.filter(
                     Q(nombre=nombre)
                    | Q(razon_social=razon_social)
                    | Q(correo=correo)
                    & Q(identificacion=identificacion)
                )
                if queryset:
                    serializacion = ConfEmpresa(queryset, many=True)
                    return Response(data=serializacion.data, status=status.HTTP_226_IM_USED)#mensaje_que esta_en uso
                else:
                    serializacion = ConfEmpresa(queryset, many=True)
                    return Response(data=serializacion.data, status=status.HTTP_200_OK)#mensaje_existoso
            except Exception as i:
                print(i)


class Usuario(APIView):
    def post(self, request):
        if self.request.data is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            usuario=self.request.data['usuario']

            try:
                queryset = ConfUsuario.objects.filter(
                    Q(usuario=usuario)
                )
                if queryset:
                    serializacion = ConfUsuario(queryset, many=True)
                    return Response(data=serializacion.data, status=status.HTTP_226_IM_USED)
                else:
                    serializacion = ConfUsuario(queryset, many=True)
                    return Response(data=serializacion.data, status=status.HTTP_200_OK)
            except Exception as o:
                print(o)









