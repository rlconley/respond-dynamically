# Generated by Django 2.2 on 2019-04-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190416_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listcity', models.CharField(max_length=100)),
            ],
        ),
    ]
