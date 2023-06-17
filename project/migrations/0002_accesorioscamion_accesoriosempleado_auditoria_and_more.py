# Generated by Django 4.2.1 on 2023-06-17 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorioscamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=100)),
                ('fechacompra', models.CharField(default=False, max_length=50)),
                ('precio', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Accesoriosempleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.CharField(default='0', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(default='', max_length=50)),
                ('empleado', models.CharField(max_length=50)),
                ('observaciones', models.TextField(max_length=300)),
                ('calificacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Camiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=50)),
                ('capacidad', models.CharField(max_length=12)),
                ('año', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=200)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checkcamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(default='', max_length=50)),
                ('empleado', models.CharField(max_length=50)),
                ('camion', models.CharField(max_length=20)),
                ('luces', models.CharField(default=True, max_length=10)),
                ('limpiaparabrizas', models.CharField(default=True, max_length=10)),
                ('frenos', models.CharField(default=True, max_length=10)),
                ('nivelfluidos', models.CharField(default=True, max_length=10)),
                ('cubiertas', models.CharField(default=True, max_length=10)),
                ('plataforma', models.CharField(default=True, max_length=10)),
                ('estructura', models.CharField(default=True, max_length=10)),
                ('amarres', models.CharField(default=True, max_length=10)),
                ('accesorios', models.CharField(default=True, max_length=10)),
                ('observaciones', models.TextField(max_length=300)),
                ('imagen', models.ImageField(null=True, upload_to='camion/')),
                ('imagen2', models.ImageField(null=True, upload_to='camion/')),
                ('firma', models.ImageField(null=True, upload_to='camion/')),
            ],
        ),
        migrations.CreateModel(
            name='Combustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(default='', max_length=50)),
                ('camion', models.CharField(max_length=20)),
                ('km', models.CharField(max_length=10)),
                ('Litros', models.CharField(max_length=10)),
                ('importe', models.CharField(default=False, max_length=20)),
                ('imagen1', models.ImageField(null=True, upload_to='camion/')),
            ],
        ),
        migrations.CreateModel(
            name='Cubierta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camion', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('kmcolocacion', models.CharField(max_length=10)),
                ('kmrotacion', models.CharField(default=True, max_length=20)),
                ('kmrecambio', models.CharField(default=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('contraseña', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(default='', max_length=50)),
                ('camion', models.CharField(max_length=20)),
                ('tema', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=10)),
                ('imagen1', models.ImageField(null=True, upload_to='camion/')),
            ],
        ),
        migrations.CreateModel(
            name='Habilitacionescamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camion', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('fechavencimiento', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jornadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empleado', models.CharField(max_length=50)),
                ('camion', models.CharField(max_length=10)),
                ('consentimiento', models.BooleanField(default=True)),
                ('entrada', models.CharField(max_length=50)),
                ('salida', models.CharField(default=None, max_length=50)),
                ('horasextras', models.CharField(default=None, max_length=1)),
                ('viaticos', models.CharField(default=None, max_length=1)),
                ('kmsalida', models.CharField(max_length=20)),
                ('kmllegada', models.CharField(default=None, max_length=20)),
                ('observaciones', models.TextField(default=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimientocamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camion', models.CharField(max_length=20)),
                ('fecha', models.CharField(default='', max_length=50)),
                ('comentarios', models.TextField(max_length=300)),
                ('imagen1', models.ImageField(null=True, upload_to='camion/')),
                ('imagen2', models.ImageField(null=True, upload_to='camion/')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('codigo', models.CharField(default=0, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Servicecamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camion', models.CharField(max_length=20)),
                ('fecharealizacion', models.CharField(default='', max_length=50)),
                ('km', models.CharField(max_length=10)),
                ('kmproximo', models.CharField(max_length=10)),
                ('detalle', models.TextField(max_length=500)),
                ('imagen1', models.ImageField(null=True, upload_to='camion/')),
            ],
        ),
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(default=True, max_length=20)),
                ('empleado', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('momentorecibida', models.CharField(default=True, max_length=50)),
                ('momentocumplida', models.CharField(default=False, max_length=50)),
                ('estado', models.CharField(default=False, max_length=20)),
                ('observacion', models.TextField(default=False, max_length=300)),
                ('imagen', models.ImageField(default=False, upload_to='visitas/')),
            ],
        ),
        migrations.CreateModel(
            name='Perfilempleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50)),
                ('empleado', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.empleados')),
            ],
        ),
        migrations.CreateModel(
            name='Habilitacionesempleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('vencimiento', models.DateField(auto_now=True)),
                ('empleado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.empleados')),
            ],
        ),
        migrations.CreateModel(
            name='DetVisitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(default=0)),
                ('observaciones', models.TextField(max_length=300)),
                ('imagen', models.ImageField(null=True, upload_to='visitas/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.productos')),
                ('visita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.visitas')),
            ],
        ),
        migrations.CreateModel(
            name='Capacitacione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realizada', models.BooleanField(default=True)),
                ('capacitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.capacitacion')),
                ('empleado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.empleados')),
            ],
        ),
        migrations.CreateModel(
            name='Accesorioentregado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaentrega', models.DateField(auto_now=True)),
                ('empleado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.empleados')),
                ('nombre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.accesoriosempleado')),
            ],
        ),
    ]
