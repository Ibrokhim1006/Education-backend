# Generated by Django 4.2.7 on 2023-11-15 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarePlanting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_plant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('care_plant_video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('care_plant_video_minutes', models.CharField(blank=True, max_length=255, null=True)),
                ('care_plant_desc', models.TextField(blank=True, null=True)),
                ('care_plant_content', models.TextField(blank=True, null=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='LocationPlantMarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(blank=True, max_length=255, null=True)),
                ('location_img', models.ImageField(blank=True, null=True, upload_to='shops/')),
                ('location_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_temperature', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_water', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_light', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_tall', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_price', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_description', models.CharField(blank=True, max_length=255, null=True)),
                ('plant_type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('plant_categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.plantcategories')),
            ],
        ),
        migrations.CreateModel(
            name='PlantRecentlyViewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('plant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.plants')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlantImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_image', models.ImageField(blank=True, null=True, upload_to='plants/')),
                ('plant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='img', to='plants.plants')),
            ],
        ),
        migrations.CreateModel(
            name='CareTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_topic_name', models.CharField(blank=True, max_length=255, null=True)),
                ('care_topic_video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('care_topic_video_minutes', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('care_plant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.careplanting')),
                ('care_topic_view_user', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CareTopicHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('care_topic_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.caretopics')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
