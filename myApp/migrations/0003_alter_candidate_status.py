# Generated by Django 3.2 on 2021-09-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20210905_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('Showed Up', 'Showed Up'), ('Showed Not', 'Showed Not')], max_length=30),
        ),
    ]
