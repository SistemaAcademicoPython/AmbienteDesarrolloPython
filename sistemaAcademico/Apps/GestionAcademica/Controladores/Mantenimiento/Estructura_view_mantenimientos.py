from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView

from sistemaAcademico.Apps.GestionAcademica import forms
from django.utils import timezone
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_conf import *
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import *
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_mant import *
import socket
from django.views.decorators.cache import cache_page

from sistemaAcademico.Apps.GestionAcademica.Forms.Admision.forms_mantenimientos import *


class Empleado(ListView):
    model = MantPersona
    queryset = model.objects.filter(Q(estado=97),
                                    Q(id_genr_tipo_usuario=20) |
                                    Q(id_genr_tipo_usuario=21)
                                    ).select_related('id_genr_tipo_usuario')
    context_object_name = 'empleado'
    template_name = 'sistemaAcademico/Admision/Mantenimiento/admision_personas.html'


class Estudiante(ListView):
    model = MantPersona
    queryset = model.objects.filter(estado=97, id_genr_tipo_usuario=19).select_related('id_genr_tipo_usuario').values(
        'id_persona', 'nombres',
        'apellidos',
        'identificacion')
    context_object_name = 'mantenimiento'
    template_name = 'sistemaAcademico/Admision/Mantenimiento/Estudiante.html'


class NuevoEmpleado(CreateView):
    model = MantPersona
    form_class = EmpleadoForm
    template_name = 'sistemaAcademico/Admision/Mantenimiento/form_reg_empleado.html'
    success_url = reverse_lazy('Academico:empleado')

    def get_context_data(self, **kwargs):
        context = super(NuevoEmpleado, self).get_context_data(**kwargs)
        pk = self.kwargs.get('id_persona', 0)
        context['id_persona'] = pk
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            empleado = form.save()
            usuario = ConfUsuario.objects.get(id_usuario=request.session.get('usuario'))
            empleado.fecha_ingreso = timezone.now()
            empleado.usuario_ing = usuario.usuario
            empleado.terminal_ing = socket.gethostname()
            id_anio_lectivo = MantAnioLectivo.objects.get(id_genr_estado=97)
            id_empleado = MantPersona.objects.get(id_persona=empleado.id_persona)
            empleado_model = MantEmpleado(id_persona=id_empleado ,id_anio_lectivo=id_anio_lectivo
                                          ,terminal_ing=socket.gethostname(),usuario_ing=usuario.usuario,fecha_ingreso=timezone.now())
            empleado_model.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UpdateEmpleado(UpdateView):
    model = MantPersona
    form_class = EditarEmpleadoForm
    template_name = 'sistemaAcademico/Admision/Mantenimiento/form_edit_empleado.html'
    success_url = reverse_lazy('Academico:empleado')
    context_object_name = 'e'


class ConsultarEmpleado(UpdateView):
    model = MantPersona
    form_class = ConsultarEmpleadoForm
    template_name = 'sistemaAcademico/Admision/Mantenimiento/form_consultar_empleado.html'
    context_object_name = 'm'

def eliminar_empleado(request, id):
    empleados = MantPersona.objects.get(id_persona=id)
    inactivo = GenrGeneral.objects.get(idgenr_general=98)
    if request.method == 'POST':
        empleados.estado = inactivo
        empleados.save()
        return redirect('Academico:empleado')
    return render(request, 'sistemaAcademico/Admision/Mantenimiento/form_eliminar_empleado.html', {'empleado': empleados})


class NuevoEstudiante(CreateView):
    model = MantPersona
    form_class = EstudianteForm
    template_name = 'sistemaAcademico/Admision/Mantenimiento/form_reg_estudiante.html'
    success_url = reverse_lazy('Academico:estudiante')

    def get_context_data(self, **kwargs):
        context = super(NuevoEstudiante, self).get_context_data(**kwargs)
        pk = self.kwargs.get('id_persona', 0)
        context['id_persona'] = pk
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            estudiante = form.save()
            usuario = ConfUsuario.objects.get(id_usuario=request.session.get('usuario'))
            estudiante.fecha_ingreso = timezone.now()
            estudiante.usuario_ing = usuario.usuario
            estudiante.terminal_ing = socket.gethostname()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ConsultarEstudiante(UpdateView):
    model = MantPersona
    form_class = ConsultarEstudianteForm
    template_name = 'sistemaAcademico/Admision/Mantenimiento/form_consultar_estudiante.html'
    context_object_name = 'm'


class UpdateEstudiante(UpdateView):
    model = MantPersona
    second_model= MovMatriculacionEstudiante
    form_class = EstudianteEditForm
    template_name = 'sistemaAcademico/Admision/Mantenimiento/form_edit_estudiante.html'
    success_url = reverse_lazy('Academico:estudiante')
    context_object_name = 'm'


class DatosEstudiante(UpdateView):
    model = MovMatriculacionEstudiante
    form_class = Editarste
    queryset = MantPersona.objects.all()
    template_name = 'sistemaAcademico/Admision/Mantenimiento/datos_estudiante_htmldepruebas.html'
    success_url = reverse_lazy('Academico:estudiante')
    context_object_name = 's'


def eliminar_estudiante(request, id):
    estudiantes = MantPersona.objects.get(id_persona=id)
    inactivo = GenrGeneral.objects.get(idgenr_general=98)
    if request.method == 'POST':
        estudiantes.estado = inactivo
        estudiantes.save()
        return redirect('Academico:estudiante')
    return render(request, 'sistemaAcademico/Admision/Mantenimiento/form_eliminar_estudiante.html', {'estudiante': estudiantes})



