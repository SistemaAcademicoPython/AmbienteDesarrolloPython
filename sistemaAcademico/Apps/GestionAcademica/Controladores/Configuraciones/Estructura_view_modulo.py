from dal import autocomplete
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_conf import ConfModulo,ConfMenu
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import GenrGeneral
from django.views.generic import ListView,CreateView,UpdateView

from sistemaAcademico.Apps.GestionAcademica.Forms.Configuracion.forms_configuraciones import modulo_form

class Modulo(ListView):
    model= ConfModulo
    queryset = model.objects.filter(id_genr_estado=97).values('id_modulo','codigo','nombre')
    context_object_name='modulo'
    template_name = 'sistemaAcademico/Configuraciones/Modulos/modulo.html'

class NuevoModulo(CreateView):
    model = ConfModulo
    form_class = modulo_form
    template_name = 'sistemaAcademico/Configuraciones/Modulos/add_modulo.html'
    success_url = reverse_lazy('Academico:modulo')

    def get_context_data(self, **kwargs):
        context = super(NuevoModulo, self).get_context_data(**kwargs)
        pk = self.kwargs.get('id_modulo', 0)
        context['id_modulo'] = pk
        return context

    def post(self, request, *args, **kargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            var_orden = 0
            c = form.save()
            lista_orden = ConfMenu.objects.filter(id_padre=0).order_by('-orden')[:1]
            for registro in lista_orden:
                b = int(registro.orden)
                var_orden = b + 1
            ConfMenu.objects.create(
                                    id_padre=0,
                                    orden=var_orden,
                                    descripcion=c.nombre,
                                    url='#',
                                    lazy_name='#',
                                    name='#',
                                    view='#',
                                    icono='#'
                                    )
            c.save()
            return redirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form))



class UpdateModulo(UpdateView):
    model = ConfModulo
    template_name = 'sistemaAcademico/Configuraciones/Modulos/editar_modulo.html'
    form_class = modulo_form
    success_url = reverse_lazy('Academico:modulo')
    context_object_name = 'm'






def editar_modulo(request,id):
    try:
        modulo = ConfModulo.objects.get(id_modulo=id);
        contexto = {}
        contexto['modulo'] =  modulo
        if request.method == 'POST':
            modulo = ConfModulo(id_modulo=id,
                                codigo=request.POST.get('codigo'),
                                nombre=request.POST.get('nombre'))
            modulo.save()
            return redirect('Academico:modulo')
    except Exception as e:
        print(e)
    
    return render(request,'sistemaAcademico/Configuraciones/Modulos/editar_modulo.html',contexto)

def eliminar_modulo(request,id):
    try:
        modulo = ConfModulo.objects.get(id_modulo=id)
        if request.method == 'POST':
           inactivo = GenrGeneral.objects.get(idgenr_general=98)
           modulo.id_genr_estado = inactivo
           modulo.save()
           return redirect('Academico:modulo')
    except Exception as e:
        raise e
    
    return render(request,'sistemaAcademico/Configuraciones/Modulos/eliminar_modulo.html',{'modulo':modulo})