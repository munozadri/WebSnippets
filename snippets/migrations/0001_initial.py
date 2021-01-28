# Generated by Django 3.0.5 on 2021-01-25 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.CharField(max_length=50, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='creado')),
                ('updated', models.DateField(auto_now_add=True, verbose_name='editado')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='descripción')),
                ('snippet', models.TextField(verbose_name='snnipet')),
                ('public', models.BooleanField(default=False, verbose_name='¿Público?')),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.Language', verbose_name='lenguaje')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Snippet',
                'verbose_name_plural': 'Snippets',
            },
        ),
    ]