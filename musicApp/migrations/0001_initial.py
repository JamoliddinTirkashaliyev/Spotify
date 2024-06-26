# Generated by Django 5.0.4 on 2024-04-13 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('sana', models.DateField()),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='albomlar/')),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiqchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('tugilgan_yil', models.DateField()),
                ('davlat', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Qoshiq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('janr', models.CharField(max_length=50)),
                ('davomiylik', models.DurationField(blank=True, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='qoshiqlar/')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicApp.albom')),
            ],
        ),
        migrations.AddField(
            model_name='albom',
            name='qoshiqchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicApp.qoshiqchi'),
        ),
    ]
