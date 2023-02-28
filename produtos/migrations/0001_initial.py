# Generated by Django 4.1.5 on 2023-02-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('abreviacao', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
