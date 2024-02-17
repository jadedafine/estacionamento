# Generated by Django 4.2.3 on 2024-02-16 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=20, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VagaEstacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numvaga', models.PositiveIntegerField()),
                ('ocupada', models.BooleanField(default=False)),
                ('entrada', models.DateTimeField(auto_now_add=True)),
                ('saida', models.DateTimeField(blank=True, null=True)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.carro')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_entrada', models.DateTimeField(auto_now_add=True)),
                ('hora_saida', models.DateTimeField(blank=True, null=True)),
                ('valor', models.FloatField(null=True)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.carro')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.vagaestacionamento')),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estacionamento.cliente'),
        ),
    ]
