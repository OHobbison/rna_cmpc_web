# Generated by Django 4.2 on 2023-05-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_id_hub_cap_alter_id_hub_ht'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id_hub',
            name='CAP',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='id_hub',
            name='HT',
            field=models.CharField(max_length=50),
        ),
    ]
