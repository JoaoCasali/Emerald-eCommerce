# Generated by Django 4.1.7 on 2023-03-02 21:52

from django.db import migrations, models
import produtos.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=produtos.models.upload_imagem_produto),
        ),
    ]
