# Generated by Django 2.2 on 2019-04-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190416_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='pleasesearch',
            name='categories',
            field=models.CharField(choices=[('Emergency', 'Emergency'), ('Food', 'Food'), ('Housing', 'Housing'), ('Goods', 'Goods'), ('Transportation', 'Transportation'), ('Health', 'Health'), ('Finances', 'Finances'), ('Care', 'Care'), ('Education', 'Education'), ('Employment', 'Employment'), ('Legal', 'Legal'), ('Communication', 'Communication'), ('One Stop', 'One Stop')], default=True, max_length=25),
            preserve_default=False,
        ),
    ]
