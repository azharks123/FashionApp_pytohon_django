# Generated by Django 4.1.2 on 2023-01-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0006_productss'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=25, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=25, null=True)),
                ('message', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
