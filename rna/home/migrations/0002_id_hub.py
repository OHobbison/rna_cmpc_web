# Generated by Django 4.2 on 2023-05-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Id_hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CD_PROC_IMPORTA_HUB', models.CharField(max_length=50)),
                ('CD_IMPORTACAO_HUB', models.CharField(max_length=50)),
                ('CD_NIVEL', models.CharField(max_length=50)),
                ('CD_MEDICAO', models.CharField(max_length=50)),
                ('CD_MEDICAO_PLANTIO', models.CharField(max_length=50)),
                ('CD_MEDICAO_PARCELA', models.CharField(max_length=50)),
                ('ID_REGIAO', models.CharField(max_length=50)),
                ('ID_PROJETO', models.CharField(max_length=50)),
                ('CD_TALHAO', models.CharField(max_length=50)),
                ('NRO_PARCELA', models.CharField(max_length=50)),
                ('NUM_FILA', models.CharField(max_length=50)),
                ('NUM_ARVORE', models.CharField(max_length=50)),
                ('NUM_FUSTE', models.CharField(max_length=50)),
                ('TIP_ARV', models.CharField(max_length=50)),
                ('CAP', models.CharField(max_length=50)),
                ('HT', models.CharField(max_length=50)),
            ],
        ),
    ]