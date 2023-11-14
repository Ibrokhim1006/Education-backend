# Generated by Django 4.2.7 on 2023-11-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_merge_20231114_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarePlantingTree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='shops/')),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
