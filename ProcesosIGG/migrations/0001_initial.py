# Generated by Django 3.2.8 on 2022-03-01 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Maestro', '0001_initial'),
        ('Anexos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('id_status', models.IntegerField(choices=[('S', 'SOLICITUD'), ('P', 'POR RETIRAR'), ('R', 'RETIRADO'), ('U', 'UMS PROCESADO')], default=50)),
                ('fecha', models.IntegerField(default=0)),
                ('fecha_retiro', models.DateTimeField()),
                ('fecha_traslado', models.DateTimeField()),
                ('cantidad', models.IntegerField(default=0)),
                ('conductor', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=10)),
                ('guia', models.CharField(max_length=30)),
                ('observacion', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=2)),
                ('eliminar', models.IntegerField(default=0)),
                ('contacto', models.CharField(max_length=50)),
                ('fecha_recibido', models.DateTimeField()),
                ('recibido', models.CharField(max_length=50)),
                ('notificacion', models.IntegerField(default=0)),
                ('fecha_notificacion', models.DateTimeField()),
                ('ums_responsable', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('clientes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.cliente')),
                ('transporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.transporte')),
            ],
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_inspired', models.IntegerField(default=0, null=True)),
                ('id_posicion', models.IntegerField(default=0, null=True)),
                ('fecha_instalacion', models.DateTimeField()),
                ('fecha_retiro', models.DateTimeField()),
                ('id_status', models.IntegerField(choices=[('D', 'DESPACHADO'), ('P', 'POR INSTALAR'), ('E', 'EN OPERACION'), ('U', 'UMS PROCESADO')], default=50)),
                ('coin_in', models.FloatField(default=0)),
                ('coin_out', models.FloatField(default=0)),
                ('handpay', models.FloatField(default=0)),
                ('jackpot', models.FloatField(default=0)),
                ('bills', models.FloatField(default=0)),
                ('plays', models.FloatField(default=0)),
                ('neto', models.FloatField(default=0)),
                ('hold', models.FloatField(default=0)),
                ('payback', models.FloatField(default=0)),
                ('eliminar', models.IntegerField(default=0)),
                ('porcentaje', models.FloatField(default=0)),
                ('impuesto', models.FloatField(default=0)),
                ('iva', models.FloatField(default=0)),
                ('otros', models.FloatField(default=0)),
                ('descuentos', models.FloatField(default=0)),
                ('dias_liquida', models.IntegerField(default=30, null=True)),
                ('fechaliquida', models.DateTimeField()),
                ('tipoliquida', models.CharField(max_length=2)),
                ('horaliquida', models.IntegerField(default=0)),
                ('variable', models.FloatField(default=0)),
                ('cobrodia', models.FloatField(default=0)),
                ('presupuestodia', models.FloatField(default=0)),
                ('cobrosoporte', models.FloatField(default=0)),
                ('montosoporte', models.FloatField(default=0)),
                ('tarifa', models.CharField(max_length=2)),
                ('nuc', models.CharField(max_length=15, null=True)),
                ('numeroresolucion', models.CharField(max_length=15, null=True)),
                ('repcoljuegos', models.CharField(max_length=15, null=True)),
                ('produccionigg', models.CharField(max_length=15, null=True)),
                ('ingreso', models.FloatField(default=0)),
                ('tipocoljuegos', models.CharField(max_length=15, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('clientes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.cliente')),
                ('id_modelo_igg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.modelo')),
                ('maquinas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.maquina')),
                ('menumix', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.menu')),
                ('razon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.razos_social')),
                ('salas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.sala')),
                ('tipooperacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.tipooperacion')),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('id_status', models.IntegerField(choices=[('C', 'CODIGOO IGG'), ('A', 'ALISTAMIENTO'), ('D', 'DESPACHADO')], default=50)),
                ('id_ano', models.IntegerField(default=0)),
                ('id_cliente', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
                ('fecha_despacho', models.DateTimeField()),
                ('contacto', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('conductor', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=10)),
                ('guia', models.CharField(max_length=30)),
                ('observacion', models.CharField(max_length=100)),
                ('eliminar', models.IntegerField(default=0)),
                ('id_seguridad', models.IntegerField(default=0)),
                ('fecha_seguridad', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('transporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.transporte')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_status', models.IntegerField(choices=[('E', 'ELABORADO'), ('P', 'PARA FIRMA'), ('DOCUM RECIBIDO', 'DOCUM RECIBIDO'), ('A', 'ANULADO')])),
                ('clase', models.CharField(choices=[('C', 'CONTRATO'), ('O', 'OTROS SI')], max_length=2)),
                ('tipo', models.CharField(choices=[('E', 'EMPRESA'), ('P', 'PERSONAL')], max_length=2)),
                ('contacto', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('fecha_contrato', models.DateTimeField()),
                ('fecha_instalacion', models.DateTimeField()),
                ('fecha_inicio', models.DateTimeField()),
                ('observacion', models.CharField(max_length=100)),
                ('eliminar', models.IntegerField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('responsable', models.CharField(max_length=50)),
                ('modelo', models.CharField(choices=[('S', 'SOLO PARTICIPACION'), ('OC', 'PARTICIPACION CON OPC COMPRA'), ('VP', 'VENTA CON PARTICIPACION'), ('V', 'VENTA SIN PARTICIPACION'), ('VF', 'VENTA CON CUOTA FIJA'), ('A', 'ARRENDAIENTO MENSUAL')], max_length=80)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('clientes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.cliente')),
                ('razon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.razos_social')),
            ],
        ),
        migrations.CreateModel(
            name='Asignacione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('id_status', models.IntegerField(choices=[('A', 'ABIERTA'), ('P', 'PRE ASIGNADO'), ('AS', 'ASIGNADO'), ('A', 'ANULADO')], default=100)),
                ('fecha', models.DateTimeField()),
                ('fecha_asignacion', models.DateTimeField()),
                ('contacto', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=100)),
                ('eliminar', models.IntegerField(default=0)),
                ('cantidad', models.IntegerField(default=0)),
                ('fecha_codigos', models.DateTimeField(default=0)),
                ('fecha_instalacion', models.DateTimeField()),
                ('notificacion', models.IntegerField(default=0)),
                ('fecha_notificacion', models.DateTimeField()),
                ('ums_responsable', models.CharField(max_length=50)),
                ('internet', models.IntegerField(default=0)),
                ('revisado', models.CharField(max_length=50)),
                ('fecha_revisado', models.DateTimeField()),
                ('modelo', models.CharField(choices=[('S', 'SOLO PARTICIPACION'), ('OC', 'PARTICIPACION CON OPC COMPRA'), ('VP', 'VENTA CON PARTICIPACION'), ('V', 'VENTA SIN PARTICIPACION'), ('VF', 'VENTA CON CUOTA FIJA'), ('A', 'ARRENDAIENTO MENSUAL')], max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('clientes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.cliente')),
                ('contrato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProcesosIGG.contrato')),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.tecnico')),
            ],
        ),
    ]
