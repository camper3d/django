# Generated by Django 5.0.4 on 2024-05-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mebel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(verbose_name='ссылка')),
                ('price', models.DecimalField(decimal_places=10, max_digits=10)),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
