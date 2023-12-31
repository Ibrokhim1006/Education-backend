# Generated by Django 4.2.7 on 2023-11-13 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authen', '0004_pyemntsumm'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuildMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriesRealEstet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Distric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NumberRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_appropriate', models.BooleanField(default=False)),
                ('apartment_area', models.CharField(blank=True, max_length=30, null=True)),
                ('house_area', models.CharField(blank=True, max_length=30, null=True)),
                ('floors_building', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_payment', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('ad_subcategory_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.adsubcategory')),
                ('ad_taype_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.adtype')),
                ('amenities_id', models.ManyToManyField(blank=True, null=True, to='real_estate.amenities')),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('build_mateial_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.buildmaterial')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.categoriesrealestet')),
                ('currency_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.currency')),
                ('distric_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.distric')),
                ('number_romm_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.numberrooms')),
                ('payment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authen.pyemntsumm')),
                ('price_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.price')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstetImgaes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='home/')),
                ('real_estet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img', to='real_estate.realestate')),
            ],
        ),
        migrations.AddField(
            model_name='realestate',
            name='repair_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.repair'),
        ),
        migrations.AddField(
            model_name='realestate',
            name='status_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.status'),
        ),
        migrations.AddField(
            model_name='distric',
            name='region_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate.region'),
        ),
        migrations.CreateModel(
            name='BuyRealEstet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('real_estet_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.realestate')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='adtype',
            name='id_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate.categoriesrealestet'),
        ),
        migrations.AddField(
            model_name='adsubcategory',
            name='id_ad_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate.adtype'),
        ),
    ]
