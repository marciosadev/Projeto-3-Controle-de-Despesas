# Generated by Django 4.1.7 on 2023-04-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('vencimento', models.DateField()),
                ('valor', models.DecimalField(decimal_places=0, max_digits=6)),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
    ]