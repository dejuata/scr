# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_tenants.postgresql_backend.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('nit', models.IntegerField(unique=True)),
                ('logo', models.ImageField(blank=True, default='', null=True, upload_to='tenant')),
                ('razon_social', models.CharField(max_length=200)),
                ('nombre_comercial', models.CharField(max_length=100, unique=True)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('departamento', models.CharField(default='', max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('direccion', models.TextField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'tenant',
                'verbose_name_plural': 'tenants',
            },
        ),
        migrations.AddField(
            model_name='domain',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='tenant.Tenant'),
        ),
    ]
