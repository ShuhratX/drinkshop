# Generated by Django 3.2.4 on 2021-06-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210612_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
    ]
