# Generated by Django 2.1.7 on 2020-10-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycourse', '0006_auto_20200818_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course_year',
            field=models.IntegerField(default=1),
        ),
    ]
