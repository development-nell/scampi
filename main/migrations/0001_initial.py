# Generated by Django 2.2.12 on 2020-10-04 00:06

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('uid', models.CharField(default='', max_length=64)),
                ('unit', django_mysql.models.EnumField(choices=[('in', 'in'), ('mm', 'mm'), ('oz', 'oz'), ('ml', 'ml'), ('hours', 'hours'), ('each', 'each')], default='each')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('unit_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('in_stock', models.IntegerField(default=0)),
                ('unit_threshold', models.IntegerField(default=0)),
                ('vendor_url', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('uid', models.CharField(default='', max_length=64)),
                ('thumbnail', models.ImageField(null=True, upload_to='')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=32)),
                ('adjustment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOptionComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units_per', models.DecimalField(decimal_places=2, max_digits=10)),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Component')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ProductOption')),
            ],
        ),
    ]
