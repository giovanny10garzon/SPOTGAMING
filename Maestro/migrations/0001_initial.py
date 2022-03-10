# Generated by Django 3.2.8 on 2022-03-01 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Anexos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CausasFalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('descripcion_sp', models.CharField(max_length=100)),
                ('descripcion_en', models.CharField(max_length=100)),
                ('observacion', models.CharField(max_length=100)),
                ('id_tipo', models.IntegerField(default=0)),
                ('activo', models.IntegerField(default=1)),
                ('eliminar', models.IntegerField(default=0)),
                ('id_seguridad', models.IntegerField(default=0)),
                ('fecha_seguridad', models.DateTimeField()),
                ('sincroniza', models.IntegerField(default=0)),
                ('fecha_sincroniza', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=15, null=True, verbose_name='NIT')),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('id_inspired', models.IntegerField(default=0, verbose_name='ID Inspired')),
                ('contacto', models.CharField(max_length=100, null=True, verbose_name='Contacto')),
                ('direccion', models.CharField(max_length=100, null=True, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=30, null=True, verbose_name='Telefono')),
                ('porcentaje', models.FloatField(default=0.0, null=True, verbose_name='% Participación')),
                ('impuesto', models.FloatField(default=353500, null=True, verbose_name='Impuesto')),
                ('iva', models.FloatField(default=137970, null=True, verbose_name='Iva')),
                ('dias_liquida', models.IntegerField(default=30, null=True, verbose_name='Días Liquidar x Mes:')),
                ('contratoCol', models.CharField(max_length=20, null=True, verbose_name='# Contrato ColJuegos:')),
                ('tipo_liquida', models.IntegerField(default=0)),
                ('liquida_mes', models.IntegerField(choices=[('M', 'MENSUAL'), ('R.F', 'RANGO DE FECHA')], default='MENSUAL', null=True, verbose_name='Metodo')),
                ('fecha_liquida', models.DateTimeField(null=True)),
                ('liquida', models.IntegerField(choices=[('U.D.M', 'ULT. DIA DELMES'), ('1RO M.S', '1RO MES SIGUIENTE'), ('F.A', 'FECHAS ALEATORIAS')], default='ULT. DIA DELMES', null=True)),
                ('descuentos', models.IntegerField(default=0, null=True, verbose_name='$ Otros Descuentos:')),
                ('presupuesto_dia', models.IntegerField(default=60000, null=True, verbose_name='$ Monto x Dia:')),
                ('dia_liquida', models.CharField(max_length=30, null=True)),
                ('hora_liquida', models.DateTimeField(default=0, null=True)),
                ('condicion', models.IntegerField(default=0, null=True)),
                ('dias_sin', models.IntegerField(default=5, null=True, verbose_name='Días Sin Transmitir:')),
                ('variable', models.IntegerField(default=12.0, null=True, verbose_name='% Variable:')),
                ('cobro_dia', models.IntegerField(default=5, null=True, verbose_name='Cobro x Días NO Transm.:')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='EMail:')),
                ('email_recaudo', models.CharField(max_length=100, null=True, verbose_name='EMail Rec. x Maquina:')),
                ('email2', models.CharField(blank=True, max_length=100, null=True, verbose_name='EMail Fallas Salas:')),
                ('email4', models.CharField(blank=True, max_length=100, null=True, verbose_name='EMail Rec. x Grupo:')),
                ('email3', models.CharField(blank=True, max_length=100, null=True, verbose_name='EMail Recaudo x Sala:')),
                ('email_fallas', models.IntegerField(default=0, null=True, verbose_name='EMail Fallas:')),
                ('email_contadores', models.IntegerField(default=0, null=True, verbose_name='EMail Contadores:')),
                ('email_sin_transmmitir', models.IntegerField(default=0, null=True, verbose_name='EMail Sin Transmitir:')),
                ('fallas', models.IntegerField(default=1, null=True)),
                ('email_recaudo_sala', models.IntegerField(default=0, null=True)),
                ('email_5', models.CharField(max_length=200, null=True)),
                ('email_recaudo_grupo', models.IntegerField(default=0, null=True)),
                ('email_6', models.CharField(max_length=200, null=True)),
                ('email_sin_transmitir_dia', models.IntegerField(default=0, null=True)),
                ('activo', models.IntegerField(default=1, null=True, verbose_name='Registro Activo')),
                ('visor', models.IntegerField(default=0, null=True, verbose_name='Incluir en el visor')),
                ('eliminar', models.IntegerField(default=0, null=True)),
                ('id_user', models.IntegerField(blank=True, default=0, null=True, verbose_name='Usuario:')),
                ('id_segurdad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_seguridad', models.DateTimeField(blank=True, null=True)),
                ('sincroniza', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_sincroniza', models.DateTimeField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('Grupos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.grupos', verbose_name='Grupo')),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.ciudad', verbose_name='Ciudad')),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.departamento', verbose_name='Departamento')),
                ('razon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.razos_social', verbose_name='Razon Social')),
            ],
        ),
        migrations.CreateModel(
            name='SolucionFalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('descripcion_sp', models.CharField(max_length=100)),
                ('descripcion_en', models.CharField(max_length=100)),
                ('observacion', models.CharField(max_length=100)),
                ('id_tipo', models.IntegerField(default=0)),
                ('id_tipo_maquina', models.IntegerField(default=0)),
                ('activo', models.IntegerField(default=1)),
                ('eliminar', models.IntegerField(default=0)),
                ('id_seguridad', models.IntegerField(default=0)),
                ('fecha_seguridad', models.DateTimeField()),
                ('sincroniza', models.IntegerField(default=0)),
                ('fecha_sincroniza', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_codigo', models.CharField(max_length=8, null=True, verbose_name='Código')),
                ('id_inspired', models.IntegerField(null=True, verbose_name='ID Inspired')),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Descripción')),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('telefono', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=100, null=True, verbose_name='E-Mail')),
                ('contacto', models.CharField(max_length=50, null=True)),
                ('fecha_liquida', models.DateTimeField(null=True)),
                ('porcentaje', models.FloatField(default=0, null=True, verbose_name='% Participación')),
                ('impuesto', models.FloatField(default=275283, null=True, verbose_name='$ Imp. ColJuegos Fijo:')),
                ('iva', models.FloatField(default=137970, null=True, verbose_name='$ IVA:')),
                ('otros', models.FloatField(default=0, null=True, verbose_name='$ Otros Gastos:')),
                ('descuentos', models.FloatField(default=0, null=True, verbose_name='$ Otros Descuentos:')),
                ('dias_liquida', models.IntegerField(default=0, null=True, verbose_name='Días Liquidar/Mes:')),
                ('tipo_liquida', models.CharField(max_length=1, null=True, verbose_name='Tiene Liq. / Cobro Fijo:')),
                ('id_tipo', models.IntegerField(choices=[('M', 'MENSUAL'), ('R.F', 'RANGO DE FECHA')], null=True, verbose_name='Metodo:')),
                ('liquida', models.IntegerField(choices=[('U.D.M', 'ULT. DIA DELMES'), ('1RO M.S', '1RO MES SIGUIENTE'), ('F.A', 'FECHAS ALEATORIAS')], default=0, null=True, verbose_name='Cierre Liquidacion:')),
                ('dia_liquida', models.CharField(default=30, max_length=2, null=True)),
                ('hora_liquida', models.DateTimeField(null=True)),
                ('email2', models.CharField(max_length=100, null=True)),
                ('email3', models.CharField(max_length=100, null=True)),
                ('email_recaudo', models.IntegerField(default=0, null=True, verbose_name='Recaudo Diario')),
                ('email_fallas', models.IntegerField(default=0, null=True, verbose_name='Fallas')),
                ('email_sin_transmitir', models.IntegerField(default=0, null=True, verbose_name='Sin Transm. Semana')),
                ('domingo', models.IntegerField(default=0, null=True)),
                ('festivos', models.IntegerField(default=0, null=True)),
                ('reporte', models.IntegerField(default=0, null=True, verbose_name='Incluir Reportes')),
                ('email_sin_transmitir_dia', models.IntegerField(default=0, null=True, verbose_name='Sin Transm. Dia')),
                ('variable', models.FloatField(default=12, null=True, verbose_name='%Variable')),
                ('cobro_dia', models.IntegerField(default=60000, null=True, verbose_name='Cobro x Días NO Transm.:\t')),
                ('presupuesto_dia', models.FloatField(default=0, null=True, verbose_name=' $ Monto x Dia:')),
                ('activo', models.IntegerField(default=1, null=True)),
                ('eliminar', models.IntegerField(blank=True, default=0, null=True)),
                ('id_seguridad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_seguridad', models.DateTimeField(blank=True, null=True)),
                ('sincroniza', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_sincroniza', models.DateTimeField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('ciudad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.ciudad')),
                ('clientes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.cliente', verbose_name='Cliente')),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.departamento')),
                ('razon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.razos_social', verbose_name='Razon Social')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=15)),
                ('razon_social', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=100)),
                ('activo', models.IntegerField(default=0)),
                ('eliminar', models.IntegerField(default=0)),
                ('id_seguridad', models.IntegerField(default=0)),
                ('fecha_seguridad', models.DateTimeField()),
                ('sincroniza', models.IntegerField(default=0)),
                ('fecha_sincroniza', models.DateTimeField()),
                ('id_clase', models.IntegerField(default=0)),
                ('id_tipo', models.CharField(max_length=1)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.ciudad')),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='ProcedimientosSFP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('titulo', models.CharField(max_length=100)),
                ('observacion', models.CharField(max_length=100)),
                ('id_tipo', models.IntegerField(default=0)),
                ('activo', models.IntegerField(default=1)),
                ('eliminar', models.IntegerField(default=0)),
                ('id_seguridad', models.IntegerField(default=0)),
                ('fecha_seguridad', models.DateTimeField()),
                ('sincroniza', models.IntegerField(default=0)),
                ('fecha_sincroniza', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('categorias', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.categoriafalla')),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_codigo', models.CharField(max_length=10, null=True, verbose_name='codigo')),
                ('id_inspired', models.IntegerField(default=0, null=True)),
                ('id_posicion', models.IntegerField(default=0, null=True)),
                ('fecha_produccion', models.DateTimeField(null=True, verbose_name='Creado')),
                ('fecha_instalacion', models.DateTimeField(null=True, verbose_name='Creado')),
                ('fecha_liquidacion', models.DateTimeField(null=True, verbose_name='Creado')),
                ('fecha_despacho', models.DateTimeField(null=True, verbose_name='Creado')),
                ('fecha_cobro', models.DateTimeField(null=True, verbose_name='Creado')),
                ('fecha_retiro', models.DateTimeField(null=True, verbose_name='Creado')),
                ('serie_PMV', models.CharField(blank=True, max_length=20, null=True)),
                ('serie_IGG', models.CharField(blank=True, max_length=20, null=True)),
                ('erial_CPU', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_HD', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_cabezal', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_staker', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_base', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_monitor1', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_monitor2', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_llave', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_printer', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_traking', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_intrusion', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_pay_link', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_fuente', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_CPU', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_HD', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_cabezal', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_staker', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_base', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_monitor1', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_monitor2', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_printer', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_traking', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_intrusion', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_pay_link', models.CharField(blank=True, max_length=50, null=True)),
                ('declara_fuente', models.CharField(blank=True, max_length=50, null=True)),
                ('DHCP', models.IntegerField(blank=True, default=0, null=True)),
                ('IP', models.CharField(blank=True, max_length=20, null=True)),
                ('mascara', models.CharField(blank=True, max_length=20, null=True)),
                ('puerta', models.CharField(blank=True, max_length=20, null=True)),
                ('DNS1', models.CharField(blank=True, max_length=20, null=True)),
                ('DNS2', models.CharField(blank=True, max_length=20, null=True)),
                ('eliminar', models.IntegerField(blank=True, default=0, null=True)),
                ('activo', models.IntegerField(blank=True, default=1, null=True)),
                ('id_seguridad', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_seguridad', models.DateTimeField(blank=True, null=True)),
                ('serial_windows', models.DateTimeField(blank=True, null=True)),
                ('liquidar', models.IntegerField(blank=True, default=0, null=True)),
                ('produccion_igg', models.CharField(blank=True, max_length=20, null=True)),
                ('modeloIGG', models.CharField(blank=True, default=0, max_length=20, null=True)),
                ('factura_PMV', models.CharField(blank=True, max_length=15, null=True)),
                ('id_contrato', models.IntegerField(blank=True, default=0, null=True, verbose_name='Liquidar Imp. Coljuegos:')),
                ('nuc', models.CharField(max_length=15, null=True)),
                ('rep_coljuegos', models.IntegerField(default=0, null=True, verbose_name='Tipo Impuesto Coljuegos:')),
                ('id_proveedor_SAS', models.IntegerField(default=0, null=True)),
                ('saskey', models.IntegerField(default=0, null=True)),
                ('soporte', models.IntegerField(default=0, null=True)),
                ('vendida', models.IntegerField(default=0, null=True)),
                ('id_tipo_maquina', models.IntegerField(default=0, null=True, verbose_name='tipo maquina')),
                ('tipo_operacion', models.CharField(max_length=2, null=True)),
                ('actualiza', models.IntegerField(blank=True, default=0)),
                ('fecha_actualiza', models.DateTimeField(blank=True, null=True)),
                ('garantia', models.IntegerField(blank=True, default=0, null=True)),
                ('fecha_soporte', models.DateTimeField(blank=True, null=True)),
                ('fecha_garantia', models.DateTimeField(blank=True, null=True)),
                ('referencia', models.CharField(blank=True, max_length=50, null=True)),
                ('observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('frozen', models.IntegerField(default=0, null=True)),
                ('fechaFrozen', models.DateTimeField(null=True)),
                ('id_grupo_frozen', models.IntegerField(default=0, null=True)),
                ('tipo_coljuegos', models.CharField(max_length=2, null=True)),
                ('reservacion', models.CharField(max_length=100, null=True)),
                ('create_at', models.DateTimeField(null=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(null=True, verbose_name='Editado')),
                ('clientes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.cliente')),
                ('familia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.familiamaquina')),
                ('id_condicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.condicion', verbose_name='Condición')),
                ('id_marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.marca')),
                ('id_modelo_igg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.modelo')),
                ('id_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.status')),
                ('menu_mix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.menu')),
                ('pripiedad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.propiedad', verbose_name='Propiedad')),
                ('razon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.razos_social', verbose_name='Razon Social')),
                ('salas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Maestro.sala')),
            ],
        ),
        migrations.CreateModel(
            name='CodigoFalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('descripcion_sp', models.CharField(max_length=100)),
                ('descripcion_en', models.CharField(max_length=100)),
                ('observacion', models.CharField(max_length=100)),
                ('id_tipo', models.IntegerField(default=0)),
                ('activo', models.IntegerField(default=1)),
                ('eliminar', models.IntegerField(default=0)),
                ('id_seguridad', models.IntegerField(default=0)),
                ('fecha_seguridad', models.DateTimeField()),
                ('sincroniza', models.IntegerField(default=0)),
                ('fecha_sincroniza', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.categoriafalla')),
            ],
        ),
    ]