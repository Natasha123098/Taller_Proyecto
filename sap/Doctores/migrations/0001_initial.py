# Generated by Django 4.2.2 on 2023-06-20 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas', models.IntegerField(null=True)),
                ('pacientes', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('edad', models.IntegerField(null=True)),
                ('años_experiencia', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True)),
                ('email', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Doctores.area')),
                ('experiencia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Doctores.experiencia')),
            ],
        ),
    ]
