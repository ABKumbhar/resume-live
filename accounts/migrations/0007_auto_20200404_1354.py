# Generated by Django 3.0.4 on 2020-04-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_grades_institute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='Institute',
            field=models.CharField(max_length=200, null='IIT Roorkee'),
        ),
    ]
