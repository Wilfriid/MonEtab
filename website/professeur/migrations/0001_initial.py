# Generated by Django 5.1 on 2024-08-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('courses', models.CharField(max_length=15)),
                ('number', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=20)),
            ],
        ),
    ]
