# Generated by Django 4.2.7 on 2023-11-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_customuser_summ'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyemntSumm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summ', models.CharField(blank=True, max_length=20, null=True)),
                ('days', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
