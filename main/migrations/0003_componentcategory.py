# Generated by Django 2.2.12 on 2020-10-04 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201004_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]
