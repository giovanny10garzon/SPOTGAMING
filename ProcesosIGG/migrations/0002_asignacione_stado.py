# Generated by Django 3.2.8 on 2022-04-11 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Anexos', '0002_statusasignacion'),
        ('ProcesosIGG', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacione',
            name='stado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Anexos.statusasignacion'),
        ),
    ]