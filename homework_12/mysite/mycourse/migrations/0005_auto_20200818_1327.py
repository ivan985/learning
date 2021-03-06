# Generated by Django 2.1.7 on 2020-08-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycourse', '0004_auto_20200818_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='mycourse.Course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(blank=True, to='mycourse.Course'),
        ),
    ]
