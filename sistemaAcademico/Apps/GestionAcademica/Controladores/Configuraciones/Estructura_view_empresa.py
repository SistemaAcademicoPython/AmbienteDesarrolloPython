from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView
from sistemaAcademico.Apps.GestionAcademica.Forms.Configuracion.forms_configuraciones import unidad_form
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_conf import *
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import *
import socket
from django.views.decorators.cache import cache_page


class NuevaEmpre(CreateView):
    model = ConfEmpresa
    template_name = 'sistemaAcademico/Configuraciones/Empresas/add_empresa.html'
    form_class = unidad_form
    success_url = reverse_lazy('Academico:empresas')

    def get_context_data(self, **kwargs):
        context = super(NuevaEmpre, self).get_context_data(**kwargs)
        pk = self.kwargs.get('id_empresa', 0)
        context['id_empresa'] = pk
        return context

    def post(self, request, *args, **kargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = ConfUsuario.objects.get(
                id_usuario=request.session.get('usuario'))
            form.fecha_ingreso = timezone.now()
            form.usuario_ing = usuario.usuario
            form.terminal_ing = socket.gethostname()
            form.save()
            return redirect(self.get_success_url())
        else:
            print("error")
            return self.render_to_response(self.get_context_data(form=form))
    """
    def form_valid(self, form):
        usuario = form['usuario'].save()
        usuario_rol = form['usuario_rol'].save(commit=False)
        usuario_rol.id_usuario = usuario
        #usuario.usuario_rol= usuario
        usuario_rol.save()
        return HttpResponseRedirect(reverse('Academico:usuarios'))
    """


class UpdateEmpre(UpdateView):
    model = ConfEmpresa
    form_class = unidad_form
    context_object_name = 'm'
    template_name = 'sistemaAcademico/Configuraciones/Empresas/editar_empresa.html'
    success_url = reverse_lazy('Academico:empresas')


def empresas(request):
    if 'usuario' in request.session:
        lista_empresa = ConfEmpresa.objects.filter(id_genr_estado=97)
        return render(request, 'sistemaAcademico/Configuraciones/Empresas/empresa.html', {'lista_empresa': lista_empresa})
    else:
        return HttpResponseRedirect('timeout/')


def nueva_empresa(request):
    if 'usuario' in request.session:
        contexto = {}
        tip_ident = GenrGeneral.objects.filter(
            tipo='TID').values('idgenr_general', 'nombre')
        contexto['tip_ident'] = tip_ident
        if request.method == 'POST':
            var_empresa_nombre = request.POST.get('nombre')
            var_rsocial = request.POST.get('rsocial')
            var_tip_ident = GenrGeneral.objects.get(
                idgenr_general=(int(request.POST.get('tip_ident'))))
            var_ident = request.POST.get('identificacion')
            direccion = request.POST.get('direccion')
            representante_legal = request.POST.get('rlegal')
            correo = request.POST.get('correo')
            telefono = request.POST.get('telefono')
            fecha_creacion = request.POST.get('f_creacion')
            nombre_equipo = socket.gethostname()
            usuario = ConfUsuario.objects.get(
                id_usuario=request.session.get('usuario'))
            menu = ConfMenu.objects.get(id_menu=23)
            estado = GenrGeneral.objects.get(idgenr_general=97)

            empresa = ConfEmpresa.objects.create(nombre=var_empresa_nombre, razon_social=var_rsocial,
                                                 id_genr_tipo_identificacion=var_tip_ident, identificacion=var_ident,
                                                 direccion=direccion, representante_legal=representante_legal, correo=correo,
                                                 telefono=telefono, fecha_creacion=fecha_creacion, id_genr_estado=estado,
                                                 fecha_ingreso=timezone.now(),
                                                 usuario_ing=usuario.usuario, terminal_ing=str(nombre_equipo))

            historial = GenrHistorial.objects.create(modulo="Configuraciones", accion="Crear", usuario_mod=usuario.usuario,
                                                     terminal_mod=str(nombre_equipo), fecha_mod=timezone.now(), id_menu=menu)

            return redirect('Academico:empresas')
        return render(request, 'sistemaAcademico/Configuraciones/Empresas/add_empresa.html', contexto)
    else:
        return HttpResponseRedirect('timeout/')


def editar_empresa(request, id):
    empresa = ConfEmpresa.objects.get(id_empresa=id)
    var_tip_ident = GenrGeneral.objects.filter(tipo='TID')
    contexto = {}
    empresa.fecha_creacion = empresa.fecha_creacion.strftime('%Y-%m-%d')
    contexto['empresa'] = empresa
    contexto['ident'] = var_tip_ident
    estado = GenrGeneral.objects.get(idgenr_general=97)
    if request.method == 'POST':
        var_empresa_nombre = request.POST.get('nombre')
        var_rsocial = request.POST.get('rsocial')
        var_tip_ident = GenrGeneral.objects.get(
            idgenr_general=(int(request.POST.get('tip_ident'))))
        var_ident = request.POST.get('identificacion')
        direccion = request.POST.get('direccion')
        representante_legal = request.POST.get('rlegal')
        correo = request.POST.get('inputEmail3')
        telefono = request.POST.get('telefono')
        fecha_creacion = request.POST.get('f_creacion')
        empresa = ConfEmpresa(id_empresa=id, nombre=var_empresa_nombre, razon_social=var_rsocial,
                              id_genr_tipo_identificacion=var_tip_ident, identificacion=var_ident,
                              direccion=direccion, representante_legal=representante_legal, correo=correo,
                              telefono=telefono, fecha_creacion=fecha_creacion,
                              id_genr_estado=estado)
        empresa.save()
        return redirect('Academico:empresas')
    return render(request, 'sistemaAcademico/Configuraciones/Empresas/Editar_empresa.html', contexto)


def eliminar_empresa(request, id):
    empresas = ConfEmpresa.objects.get(id_empresa=id)
    inactivo = GenrGeneral.objects.get(idgenr_general=98)
    if request.method == 'POST':
        empresas.id_genr_estado = inactivo
        empresas.save()
        return redirect('Academico:empresas')
    return render(request, 'sistemaAcademico/Configuraciones/Empresas/eliminar.html', {'empresa': empresas})
