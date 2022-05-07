# Generated by Django 4.0.4 on 2022-05-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=250)),
                ('buy_date', models.DateField(auto_now_add=True, verbose_name='Fecha de compra')),
                ('marca', models.CharField(max_length=250)),
            ],
        ),
    ]
