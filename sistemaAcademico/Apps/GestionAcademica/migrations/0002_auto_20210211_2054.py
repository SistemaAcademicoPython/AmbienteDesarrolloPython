# Generated by Django 2.2.5 on 2021-02-12 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAcademica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantpersona',
            name='categoria_doc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='fech_sal_jor',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='fecha_ingreso_jor',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='mot_ingreso',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='mot_salida',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='nombre_titulo1',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='nombre_titulo2',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='nombre_titulo3',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='titulo1_nivel3',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='titulo1_nivel4',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mantpersona',
            name='titulo2_nivel3',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mantpersona',
            name='fecha_ingreso',
            field=models.DateField(null=True),
        ),
    ]
