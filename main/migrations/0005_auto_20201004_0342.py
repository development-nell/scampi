# Generated by Django 2.2.12 on 2020-10-04 03:42

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_component_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='productoption',
            name='produced',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productoption',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='productoptioncomponent',
            name='units_per',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.CreateModel(
            name='ProductionQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.IntegerField(default=0)),
                ('status', django_mysql.models.EnumField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold')], default='Pending')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ProductOption')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('units_produced', models.IntegerField(default=0)),
                ('production_queue', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.ProductionQueue')),
            ],
        ),
    ]