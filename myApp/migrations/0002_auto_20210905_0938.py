# Generated by Django 3.2 on 2021-09-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='remark',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('Showed Up', 'Showed Up'), ('Showed Not', 'Showed Not')], max_length=150),
        ),
    ]
