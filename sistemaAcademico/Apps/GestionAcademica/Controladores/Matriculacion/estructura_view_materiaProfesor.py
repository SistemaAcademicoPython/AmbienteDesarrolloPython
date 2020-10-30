from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_genr import *
from sistemaAcademico.Apps.GestionAcademica.Diccionario.Estructuras_tablas_mov import *
from sistemaAcademico.Apps.GestionAcademica.Forms.Matriculacion.forms_mov_anio_curso import MovMateriaProfesorForm
from django.contrib import messages
from django.db.models import Q

class MovMateriProfesorList(UpdateView):
    model = Mov_Materia_profesor
    template_name = 'sistemaAcademico/Matriculacion/HorarioMod/horarioMod.html'
    form_class = MovMateriaProfesorForm
    success_url = reverse_lazy('Academico:asignacion_materiasprof')

    def post(self, request, **kwargs):
        self.object = self.get_object() 
        request.POST = request.POST.copy()
        lista =[]
        id_materia_profesor = kwargs['pk']
        form = self.form_class(request.POST)

        for i in request.POST['id_detalle_materia_curso']:
            print(i)
            value_materia= Mov_Materia_profesor.objects.filter(id_detalle_materia_curso=i).filter(~Q(id_empleado = request.POST['id_empleado'])).count()
            if value_materia>0:
                
                materia = MovDetalleMateriaCurso.objects.get(id_detalle_materia_curso=i)
                lista.append(materia)
            else:
                continue
        if len(lista)>0:
            for i in lista:
                
                materia =i.id_genr_materias.nombre
                curso = i.id_mov_anio_lectivo_curso.id_curso.nombre
                paralelo = i.id_mov_anio_lectivo_curso.id_genr_paralelo.nombre
                formacion = i.id_mov_anio_lectivo_curso.id_curso.id_genr_formacion.nombre
                messages.error(request,"{0} del curso {1}/{2} {3} ya se encuentra asignada".format(materia,curso,paralelo,formacion))

            return self.render_to_response(self.get_context_data())
        else:
        
            return super(MovMateriProfesorList, self).post(request, **kwargs)

            
          



