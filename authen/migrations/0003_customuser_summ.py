# Generated by Django 4.2.7 on 2023-11-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_checksms'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='summ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
