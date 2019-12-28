from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.utils import timezone
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_conf import *
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import *
import socket
from django.views.decorators.cache import cache_page

cache_page(60*15)
def perfiles(request):
    #-----Valida si la sesion sigue activa sino regresa al login.html
    if 'usuario' in request.session:
        permiso=ConfPermiso.objects.filter(id_genr_estado=97).values('id_permiso','id_menu','id_modulo','id_genr_estado')
        print(permiso)
        return render(request,'sistemaAcademico/Configuraciones/Permisos/permisos.html',{'permiso': permiso})
    else:
        return HttpResponseRedirect('timeout/')


def add_permiso(request):
    if 'usuario' in request.session:
        contexto={}
        menu=ConfMenu.objects.filter(id_genr_estado=97)
        modulo=ConfModulo.objects.filter(id_genr_estado=97)
        estado = GenrGeneral.objects.filter(tipo='STA')
        contexto['modulo']=modulo
        contexto['estado'] = estado
        contexto['menu'] = menu
        if request.method == 'POST':
            menu=ConfMenu.objects.get(id_menu=int(request.POST.get('menu')))
            #var_usuario = request.POST.get('usuario')
            modulo=ConfModulo.objects.get(id_modulo=int(request.POST.get('modulo')))
            permiso=GenrGeneral.objects.get(idgenr_general=int(request.POST.get('estado')))
            guardar_pemiso = ConfPermiso(id_menu=menu,id_modulo=modulo,id_genr_estado=permiso)
            guardar_pemiso.save()
            return redirect('Academico:perfiles')

        return render(request, 'sistemaAcademico/Configuraciones/Permisos/add_permisos.html',contexto)
    else:
        return HttpResponseRedirect('timeout/')



def editar_permiso(request,id):
    contexto={}
    modulo = ConfModulo.objects.filter(id_genr_estado=97)
    estado = GenrGeneral.objects.filter(tipo='STA')
    menu= ConfMenu.objects.all()
    contexto['modulo'] = modulo
    contexto['estado'] = estado
    contexto['menu']=menu
    permiso=ConfPermiso.objects.all()
    contexto['permiso']= permiso
    if request.method == 'POST':
        menu = ConfMenu.objects.get(id_menu=int(request.POST.get('menu')))
        modulo = ConfModulo.objects.get(id_modulo=int(request.POST.get('modulo')))
        est = GenrGeneral.objects.get(idgenr_general=int(request.POST.get('estado')))
        print(menu)
        guardar_pemiso = ConfPermiso(id_permiso=id,id_menu=menu, id_modulo=modulo, id_genr_estado=est)
        guardar_pemiso.save(force_update=True)
        return redirect('Academico:perfiles')


    return render (request,'sistemaAcademico/Configuraciones/Permisos/editar_permiso.html',contexto)