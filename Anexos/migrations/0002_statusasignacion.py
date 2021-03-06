# Generated by Django 3.2.8 on 2022-04-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anexos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusAsignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.IntegerField(default=1, null=True)),
                ('eliminar', models.IntegerField(default=0, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
        ),
    ]
