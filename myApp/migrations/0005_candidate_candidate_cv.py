# Generated by Django 3.2 on 2021-09-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20210910_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='candidate_cv',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
