# Generated by Django 4.2.7 on 2023-11-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_course_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='summ_course',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
