# Generated by Django 2.2.5 on 2020-02-12 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfAccion',
            fields=[
                ('id_accion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Accion',
                'verbose_name_plural': 'Acciones',
                'db_table': 'conf_accion',
            },
        ),
        migrations.CreateModel(
            name='ConfCorreosSmpt',
            fields=[
                ('id_correos_smpt', models.AutoField(primary_key=True, serialize=False)),
                ('ssl', models.CharField(max_length=30)),
                ('dominio', models.CharField(max_length=30)),
                ('puerto', models.CharField(max_length=20)),
                ('usuario_c', models.CharField(max_length=100)),
                ('contraseña_c', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': ('Correos Smpt',),
                'verbose_name_plural': ('Correos Smpt',),
                'db_table': 'conf_correos_smpt',
            },
        ),
        migrations.CreateModel(
            name='ConfMenu',
            fields=[
                ('id_menu', models.AutoField(primary_key=True, serialize=False)),
                ('id_padre', models.IntegerField()),
                ('orden', models.IntegerField()),
                ('descripcion', models.CharField(db_column='descripcion', max_length=45)),
                ('url', models.CharField(max_length=60)),
                ('icono', models.CharField(default='#', max_length=50)),
                ('lazy_name', models.CharField(default='example/', max_length=60)),
                ('name', models.CharField(default='example', max_length=60)),
                ('view', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': ('Menu',),
                'verbose_name_plural': ('Menu',),
                'db_table': 'conf_menu',
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='ConfModulo',
            fields=[
                ('id_modulo', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': ('Modulo',),
                'verbose_name_plural': ('Modulos',),
                'db_table': 'conf_modulo',
            },
        ),
        migrations.CreateModel(
            name='ConfModulo_menu',
            fields=[
                ('id_modulo_menu', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Modulo_Menu',
                'verbose_name_plural': 'Modulos_Menus',
                'db_table': 'conf_modulo_menu',
            },
        ),
        migrations.CreateModel(
            name='ConfRol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': ('Rol',),
                'verbose_name_plural': ('Roles',),
                'db_table': 'conf_rol',
            },
        ),
        migrations.CreateModel(
            name='ConfUsuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=45)),
                ('clave', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': ('Usuario',),
                'verbose_name_plural': ('Usuarios',),
                'db_table': 'conf_usuario',
            },
        ),
        migrations.CreateModel(
            name='GenrGeneral',
            fields=[
                ('idgenr_general', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': ('Lista',),
                'verbose_name_plural': ('Listas',),
                'db_table': 'genr_general',
            },
        ),
        migrations.CreateModel(
            name='MantAnioLectivo',
            fields=[
                ('id_anio_lectivo', models.AutoField(primary_key=True, serialize=False)),
                ('anio', models.IntegerField()),
                ('ciclo', models.IntegerField()),
                ('fecha_incio_ciclo', models.DateField()),
                ('fecha_fin_ciclo', models.DateField()),
                ('id_genr_estado', models.ForeignKey(db_column='id_genr_estado', on_delete=django.db.models.deletion.CASCADE, related_name='fk_aniolectivo_estado', to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': ('Año lectivo',),
                'verbose_name_plural': ('Año lectivo',),
                'db_table': 'mant_anio_lectivo',
            },
        ),
        migrations.CreateModel(
            name='MantEmpleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField()),
                ('usuario_ing', models.CharField(max_length=45)),
                ('terminal_ing', models.CharField(max_length=45)),
                ('id_anio_lectivo', models.ForeignKey(db_column='id_anio_lectivo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_empleado_anio_lectivo', to='GestionAcademica.MantAnioLectivo')),
            ],
            options={
                'verbose_name': ('Empleado',),
                'verbose_name_plural': ('Empleados',),
                'db_table': 'mant_empleado',
            },
        ),
        migrations.CreateModel(
            name='MantEstudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_estudiante', models.CharField(max_length=45)),
                ('fecha_ingreso', models.DateTimeField()),
                ('usuario_ing', models.CharField(max_length=45)),
                ('terminal_ing', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': ('Estudiante',),
                'verbose_name_plural': ('Estudiantes',),
                'db_table': 'mant_estudiante',
            },
        ),
        migrations.CreateModel(
            name='MantPersona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField()),
                ('estado', models.IntegerField()),
                ('identificacion', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateTimeField()),
                ('usuario_ing', models.CharField(max_length=60)),
                ('terminal_ing', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=150)),
                ('celular', models.CharField(max_length=15)),
                ('lugar_nacimiento', models.CharField(max_length=45)),
                ('discapacidad', models.BooleanField()),
                ('discapacidad_renal', models.BooleanField()),
                ('discapacidad_neurologica', models.BooleanField()),
                ('enfermedad_alergica', models.BooleanField()),
                ('asma', models.BooleanField()),
                ('epilepsia', models.BooleanField()),
                ('enfermedad_congenita', models.BooleanField()),
                ('enfermedad_respiratoria', models.BooleanField()),
                ('atencion_psicologica', models.BooleanField()),
                ('bono_solidario', models.BooleanField()),
                ('mienbros_hogar', models.IntegerField()),
                ('pnombres', models.CharField(default='no requerido', max_length=45, null=True)),
                ('papellidos', models.CharField(default='no requerido', max_length=45, null=True)),
                ('pidentificacion', models.CharField(default='no requerido', max_length=15, null=True, unique=True)),
                ('pdireccion', models.CharField(default='no requerido', max_length=45, null=True)),
                ('ptelefono', models.CharField(default='no requerido', max_length=45, null=True)),
                ('pvive_con_usted', models.BooleanField(default=0, null=True)),
                ('mnombres', models.CharField(default='no requerido', max_length=45, null=True)),
                ('mapellidos', models.CharField(default='no requerido', max_length=45, null=True)),
                ('mdireccion', models.CharField(default='no requerido', max_length=45, null=True)),
                ('mtelefono', models.CharField(default='no requerido', max_length=45, null=True)),
                ('midentificacion', models.CharField(default='no requerido', max_length=15, null=True, unique=True)),
                ('mvive_con_usted', models.BooleanField(default=0, null=True)),
                ('rnombres', models.CharField(default='no requerido', max_length=45, null=True)),
                ('rapellidos', models.CharField(default='no requerido', max_length=45, null=True)),
                ('rtelefono', models.CharField(default='no requerido', max_length=45, null=True)),
                ('rvive_con_usted', models.BooleanField(default=0, null=True)),
                ('ridentificacion', models.CharField(default='no requerido', max_length=13, null=True, unique=True)),
                ('id_genr_categoria_migratoria', models.ForeignKey(db_column='id_genr_categoria_migratoria', on_delete=django.db.models.deletion.CASCADE, related_name='categoria_migratoria', to='GestionAcademica.GenrGeneral')),
                ('id_genr_ciudad', models.ForeignKey(db_column='id_genr_ciudad', on_delete=django.db.models.deletion.CASCADE, related_name='ciudad', to='GestionAcademica.GenrGeneral')),
                ('id_genr_estado_civil', models.ForeignKey(db_column='id_genr_estado_civil', on_delete=django.db.models.deletion.CASCADE, related_name='estado_civil', to='GestionAcademica.GenrGeneral')),
                ('id_genr_estado_laboralm', models.ForeignKey(db_column='id_genr_estado_laboralm', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='estado_laboralm', to='GestionAcademica.GenrGeneral')),
                ('id_genr_estado_laboralp', models.ForeignKey(db_column='id_genr_estado_laboralp', on_delete=django.db.models.deletion.CASCADE, related_name='estado_laboralp', to='GestionAcademica.GenrGeneral')),
                ('id_genr_etnia', models.ForeignKey(db_column='id_genr_etnia', on_delete=django.db.models.deletion.CASCADE, related_name='etnia', to='GestionAcademica.GenrGeneral')),
                ('id_genr_genero', models.ForeignKey(db_column='id_genr_genero', on_delete=django.db.models.deletion.CASCADE, related_name='genero', to='GestionAcademica.GenrGeneral')),
                ('id_genr_idioma_ancestral', models.ForeignKey(db_column='id_genr_idioma_ancestral', on_delete=django.db.models.deletion.CASCADE, related_name='acestral', to='GestionAcademica.GenrGeneral')),
                ('id_genr_indigena', models.ForeignKey(db_column='id_genr_indigena', on_delete=django.db.models.deletion.CASCADE, related_name='indigena', to='GestionAcademica.GenrGeneral')),
                ('id_genr_jornada', models.ForeignKey(db_column='id_genr_jornada', on_delete=django.db.models.deletion.CASCADE, related_name='jornada', to='GestionAcademica.GenrGeneral')),
                ('id_genr_pais', models.ForeignKey(db_column='id_genr_pais', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral')),
                ('id_genr_provincia', models.ForeignKey(db_column='id_genr_provincia', on_delete=django.db.models.deletion.CASCADE, related_name='provincia', to='GestionAcademica.GenrGeneral')),
                ('id_genr_tipo_identificacion', models.ForeignKey(db_column='id_genr_tipo_identificacion', on_delete=django.db.models.deletion.CASCADE, related_name='identificacion', to='GestionAcademica.GenrGeneral')),
                ('id_genr_tipo_parentesco', models.ForeignKey(db_column='id_genr_tipo_parentesco', default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tipo_parentesco', to='GestionAcademica.GenrGeneral')),
                ('id_genr_tipo_sangre', models.ForeignKey(db_column='id_genr_tipo_sangre', on_delete=django.db.models.deletion.CASCADE, related_name='tipo_de_sangre', to='GestionAcademica.GenrGeneral')),
                ('id_genr_tipo_usuario', models.ForeignKey(db_column='id_genr_tipo_usuario', on_delete=django.db.models.deletion.CASCADE, related_name='persona_tipo_usuario', to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': ('Persona',),
                'verbose_name_plural': ('Personas',),
                'db_table': 'mant_persona',
            },
        ),
        migrations.CreateModel(
            name='MovCabCurso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=10)),
                ('cupo', models.IntegerField()),
                ('id_anio_lectivo', models.ForeignKey(db_column='id_anio_lectivo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_aniolectivo', to='GestionAcademica.MantAnioLectivo')),
                ('id_genr_curso', models.ForeignKey(db_column='id_genr_curso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_curso', to='GestionAcademica.GenrGeneral')),
                ('id_genr_formacion', models.ForeignKey(db_column='id_genr_formacion', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_formacion', to='GestionAcademica.GenrGeneral')),
                ('id_genr_jornada', models.ForeignKey(db_column='id_genr_jornada', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_jornada', to='GestionAcademica.GenrGeneral')),
                ('id_genr_paralelo', models.ForeignKey(db_column='id_genr_paralelo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_cabcurso_paralelo', to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'mov_cab_curso',
            },
        ),
        migrations.CreateModel(
            name='MovMatriculacionEstudiante',
            fields=[
                ('id_matriculacion_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('id_anio_lectivo', models.ForeignKey(db_column='id_anio_lectivo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_matriculacionestudiante_aniolectivo', to='GestionAcademica.MantAnioLectivo')),
                ('id_curso', models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_matriculacionestudiante_cabcurso', to='GestionAcademica.MovCabCurso')),
                ('id_estudiante', models.ForeignKey(db_column='id_estudiante', on_delete=django.db.models.deletion.CASCADE, related_name='fk_matriculacionestudiante_estudiante', to='GestionAcademica.MantEstudiante')),
            ],
            options={
                'verbose_name': 'Matriculacion estudiante',
                'verbose_name_plural': 'Matriculacion estudiante',
                'db_table': 'mov_matriculacion_estudiante',
            },
        ),
        migrations.CreateModel(
            name='MovEstudianteAsignacionCurso',
            fields=[
                ('id_estudiante_curso', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_ingreso', models.DateTimeField()),
                ('usuario_ing', models.CharField(max_length=45)),
                ('terminal_ing', models.CharField(max_length=45)),
                ('id_curso', models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_estudianteAsignacioncurso_movcabcurso', to='GestionAcademica.MovCabCurso')),
                ('id_estudiante', models.ForeignKey(db_column='id_estudiante', on_delete=django.db.models.deletion.CASCADE, related_name='fk_estudianteAsignacioncurso_estudiante', to='GestionAcademica.MantEstudiante')),
            ],
            options={
                'verbose_name': 'Asignacion de curso',
                'verbose_name_plural': 'Asignacion de curso',
                'db_table': 'mov_estudiante_asignacion_curso',
            },
        ),
        migrations.CreateModel(
            name='MovDetalleRegistroNotas',
            fields=[
                ('id_detalle_registro_notas', models.AutoField(primary_key=True, serialize=False)),
                ('primer_parcial', models.FloatField()),
                ('segundo_parcial', models.FloatField()),
                ('tercer_parcial', models.FloatField()),
                ('examen', models.FloatField()),
                ('promedio', models.FloatField()),
                ('total_promedio_general', models.FloatField()),
                ('id_estudiante', models.ForeignKey(db_column='id_estudiante', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detalleregistronotas_estudiante', to='GestionAcademica.MantEstudiante')),
                ('id_general_quimestre', models.ForeignKey(db_column='id_general_quimestre', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detalleregistronotas_quimestre', to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': 'Detalle Registro de Curso',
                'verbose_name_plural': 'Detalle Registro de Curso',
                'db_table': 'mov_detalle_registro_notas',
            },
        ),
        migrations.CreateModel(
            name='MovDetalleMateriaCurso',
            fields=[
                ('id_detalle_curso', models.AutoField(primary_key=True, serialize=False)),
                ('anio', models.IntegerField()),
                ('estado', models.ForeignKey(db_column='estado', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detallemateriacurso_estado', to='GestionAcademica.GenrGeneral')),
                ('id_curso', models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detallemateriacurso_cabcurso', to='GestionAcademica.MovCabCurso')),
                ('id_genr_materias', models.ForeignKey(db_column='id_genr_materias', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detallemateriacurso_materias', to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': 'Detalle Materia Curso',
                'verbose_name_plural': 'Detalle Materia Curso',
                'db_table': 'mov_detalle_materia_curso',
            },
        ),
        migrations.CreateModel(
            name='MovDetalleEmpleado',
            fields=[
                ('id_detalle_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('id_anio_lectivo', models.ForeignKey(db_column='id_anio_lectivo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detalleEmpleado_aniolectivo', to='GestionAcademica.GenrGeneral')),
                ('id_curso', models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detalleEmpleado_cabcurso', to='GestionAcademica.MovCabCurso')),
                ('id_genr_materia', models.ForeignKey(db_column='id_genr_materia', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detalleEmpleado_materia', to='GestionAcademica.GenrGeneral')),
                ('id_genr_paralelo', models.ForeignKey(db_column='id_genr_paralelo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_detalleEmpleado_paralelo', to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': 'Detalle Empleado',
                'verbose_name_plural': 'Detalle Empleados',
                'db_table': 'mov_detalle_empleado',
            },
        ),
        migrations.CreateModel(
            name='MovCabRegistroNotas',
            fields=[
                ('id_registro_notas', models.AutoField(primary_key=True, serialize=False)),
                ('promedio_curso_1q', models.FloatField()),
                ('promedio_curso_2q', models.FloatField()),
                ('promedio_curso_general', models.FloatField()),
                ('id_anio_lectivo', models.ForeignKey(db_column='id_anio_lectivo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_registronotas_anniolectivo', to='GestionAcademica.MantAnioLectivo')),
                ('id_curso', models.ForeignKey(db_column='id_curso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_registronotas_cabcurso', to='GestionAcademica.MovCabCurso')),
                ('id_empleado', models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.CASCADE, related_name='fk_registronotas_empleado', to='GestionAcademica.MantEmpleado')),
                ('id_genr_materia', models.ForeignKey(db_column='id_genr_materia', on_delete=django.db.models.deletion.CASCADE, related_name='fk_registronotas_materia', to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': 'Registro Notas',
                'verbose_name_plural': 'Registro Notas',
                'db_table': 'mov_cab_registro_notas',
            },
        ),
        migrations.CreateModel(
            name='MovAdmision',
            fields=[
                ('id_admision', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=45)),
                ('documento', models.CharField(max_length=45)),
                ('id_estudiante', models.ForeignKey(db_column='id_estudiante', on_delete=django.db.models.deletion.CASCADE, related_name='fk_admision_estudiante', to='GestionAcademica.MantEstudiante')),
            ],
            options={
                'verbose_name': 'Admision',
                'verbose_name_plural': 'Admisiones',
                'db_table': 'mov_admision',
            },
        ),
        migrations.CreateModel(
            name='MantRepresentante',
            fields=[
                ('id_representante', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_ing', models.CharField(max_length=45)),
                ('fecha_ingreso', models.DateTimeField()),
                ('terminal_ing', models.CharField(max_length=45)),
                ('ingresos_totales', models.FloatField()),
                ('id_usuario', models.IntegerField()),
                ('id_genr_nivel_formacion', models.ForeignKey(db_column='id_genr_nivel_formacion', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral')),
                ('id_persona', models.ForeignKey(db_column='id_persona', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.MantPersona')),
            ],
            options={
                'verbose_name': ('Representante',),
                'verbose_name_plural': ('Representantes',),
                'db_table': 'mant_representante',
            },
        ),
        migrations.AddField(
            model_name='mantestudiante',
            name='id_persona',
            field=models.ForeignKey(db_column='id_persona', on_delete=django.db.models.deletion.CASCADE, related_name='fk_estudiante_persona', to='GestionAcademica.MantPersona'),
        ),
        migrations.AddField(
            model_name='mantempleado',
            name='id_detalle_empleado',
            field=models.ForeignKey(db_column='id_detalle_empleado', on_delete=django.db.models.deletion.CASCADE, related_name='fk_empleado_detalle', to='GestionAcademica.MovDetalleEmpleado'),
        ),
        migrations.AddField(
            model_name='mantempleado',
            name='id_persona',
            field=models.ForeignKey(db_column='id_persona', on_delete=django.db.models.deletion.CASCADE, related_name='fk_empleado_persona', to='GestionAcademica.MantPersona'),
        ),
        migrations.AddField(
            model_name='mantempleado',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, related_name='fk_empleado_usuario', to='GestionAcademica.ConfUsuario'),
        ),
        migrations.CreateModel(
            name='GenrHistorial',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('modulo', models.CharField(max_length=50)),
                ('accion', models.CharField(max_length=50)),
                ('usuario_mod', models.CharField(max_length=50)),
                ('terminal_mod', models.CharField(max_length=50)),
                ('fecha_mod', models.DateField()),
                ('id_menu', models.ForeignKey(db_column='id_menu', on_delete=django.db.models.deletion.CASCADE, related_name='fk_genrhistorial_confmenu', to='GestionAcademica.ConfMenu')),
            ],
            options={
                'verbose_name': ('Lista',),
                'verbose_name_plural': ('Listas',),
                'db_table': 'genr_historial',
            },
        ),
        migrations.CreateModel(
            name='ConfUsuario_rol',
            fields=[
                ('id_usuario_rol', models.AutoField(primary_key=True, serialize=False)),
                ('id_rol', models.ForeignKey(db_column='id_rol', on_delete=django.db.models.deletion.CASCADE, related_name='fkrol_usuario', to='GestionAcademica.ConfRol')),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, related_name='fkusuario_rol', to='GestionAcademica.ConfUsuario')),
            ],
            options={
                'verbose_name': ('Rol de usuario',),
                'verbose_name_plural': ('Roles de usuarios',),
                'db_table': 'conf_usuario_rol',
            },
        ),
        migrations.AddField(
            model_name='confusuario',
            name='id_genr_estado',
            field=models.ForeignKey(db_column='id_genr_estado', on_delete=django.db.models.deletion.CASCADE, related_name='fk_usuario_estado', to='GestionAcademica.GenrGeneral'),
        ),
        migrations.AddField(
            model_name='confusuario',
            name='id_genr_tipo_usuario',
            field=models.ForeignKey(db_column='id_genr_tipo_usuario', on_delete=django.db.models.deletion.CASCADE, related_name='fk_usuario_tipo_usuario', to='GestionAcademica.GenrGeneral'),
        ),
        migrations.AddField(
            model_name='confusuario',
            name='id_persona',
            field=models.ForeignKey(db_column='id_persona', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.MantPersona'),
        ),
        migrations.AddField(
            model_name='confrol',
            name='id_genr_estado',
            field=models.ForeignKey(db_column='id_genr_estado', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral'),
        ),
        migrations.CreateModel(
            name='ConfPermiso',
            fields=[
                ('id_permiso', models.AutoField(primary_key=True, serialize=False)),
                ('id_modulo_menu', models.ForeignKey(db_column='id_modulo_menu', on_delete=django.db.models.deletion.CASCADE, related_name='fk_permiso_modmenu', to='GestionAcademica.ConfModulo_menu')),
                ('id_usuario_rol', models.ForeignKey(db_column='id_usuario_rol', on_delete=django.db.models.deletion.CASCADE, related_name='fk_permiso_usurol', to='GestionAcademica.ConfUsuario_rol')),
            ],
            options={
                'verbose_name': ('Permiso',),
                'verbose_name_plural': ('Permisos',),
                'db_table': 'conf_permiso',
            },
        ),
        migrations.AddField(
            model_name='confmodulo_menu',
            name='id_genr_estado',
            field=models.ForeignKey(db_column='id_genr_estado', default='97', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral'),
        ),
        migrations.AddField(
            model_name='confmodulo_menu',
            name='id_menu',
            field=models.ForeignKey(db_column='id_menu', on_delete=django.db.models.deletion.CASCADE, related_name='fk_modmen_menu', to='GestionAcademica.ConfMenu'),
        ),
        migrations.AddField(
            model_name='confmodulo_menu',
            name='id_modulo',
            field=models.ForeignKey(db_column='id_modulo', on_delete=django.db.models.deletion.CASCADE, related_name='fk_modmen_modulo', to='GestionAcademica.ConfModulo'),
        ),
        migrations.AddField(
            model_name='confmodulo',
            name='id_genr_estado',
            field=models.ForeignKey(db_column='id_genr_estado', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral'),
        ),
        migrations.AddField(
            model_name='confmenu',
            name='id_genr_estado',
            field=models.ForeignKey(db_column='id_genr_estado', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral'),
        ),
        migrations.CreateModel(
            name='ConfEmpresa',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('razon_social', models.CharField(max_length=200)),
                ('identificacion', models.CharField(max_length=50, unique=True)),
                ('direccion', models.CharField(max_length=50)),
                ('representante_legal', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('usuario_ing', models.CharField(max_length=45)),
                ('terminal_ing', models.CharField(max_length=45)),
                ('id_genr_estado', models.ForeignKey(db_column='estado', on_delete=django.db.models.deletion.CASCADE, related_name='estado_empresa', to='GestionAcademica.GenrGeneral')),
                ('id_genr_tipo_identificacion', models.ForeignKey(db_column='id_genr_tipo_identificacion', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral')),
            ],
            options={
                'verbose_name': ('Empresa',),
                'verbose_name_plural': ('Empresas',),
                'db_table': 'conf_empresa',
            },
        ),
        migrations.CreateModel(
            name='ConfDetallePermiso',
            fields=[
                ('id_detalle_permiso', models.AutoField(primary_key=True, serialize=False)),
                ('id_accion', models.ForeignKey(db_column='id_accion', on_delete=django.db.models.deletion.CASCADE, related_name='fk_det_permiso_accion', to='GestionAcademica.ConfAccion')),
                ('id_genr_estado', models.ForeignKey(db_column='id_genr_estado', on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.GenrGeneral')),
                ('id_menu', models.ForeignKey(db_column='id_menu', on_delete=django.db.models.deletion.CASCADE, related_name='fk_det_permiso_menu', to='GestionAcademica.ConfMenu')),
                ('id_permiso', models.ForeignKey(db_column='id_permiso', on_delete=django.db.models.deletion.CASCADE, related_name='fk_det_permiso_cab_permiso', to='GestionAcademica.ConfPermiso')),
            ],
            options={
                'verbose_name': ('Detalle Permiso',),
                'verbose_name_plural': ('Detalle Permisos',),
                'db_table': 'conf_detalle_permiso',
            },
        ),
        migrations.AddField(
            model_name='confaccion',
            name='id_genr_estado',
            field=models.ForeignKey(db_column='id_genr_estado', on_delete=django.db.models.deletion.CASCADE, related_name='fk_accion_genr', to='GestionAcademica.GenrGeneral'),
        ),
        migrations.AddField(
            model_name='confaccion',
            name='id_menu',
            field=models.ForeignKey(db_column='id_menu', on_delete=django.db.models.deletion.CASCADE, related_name='fk_accion_menu', to='GestionAcademica.ConfMenu'),
        ),
    ]
