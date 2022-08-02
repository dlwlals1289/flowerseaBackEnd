<<<<<<< HEAD
# Generated by Django 4.0.6 on 2022-07-29 08:18
=======
# Generated by Django 4.0.6 on 2022-07-31 13:07
>>>>>>> hoo

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('shopName', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=300)),
                ('phoneNum', models.CharField(max_length=20)),
                ('openHours', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubFlower',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('flowerName', models.CharField(max_length=100)),
                ('oneFlowerPrice', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('enlightened', models.CharField(choices=[('no bloom', '개화 안함'), ('start bloom', '개화 초기'), ('full bloom', '만개')], default='full bloom', max_length=50)),
                ('floriography', models.CharField(max_length=100)),
                ('flowerPhoto', models.ImageField(blank=True, null=True, upload_to='subflower/')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.shop')),
            ],
        ),
        migrations.CreateModel(
            name='MainFlower',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('flowerName', models.CharField(max_length=100)),
                ('oneFlowerPrice', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('enlightened', models.CharField(choices=[('no bloom', '개화 안함'), ('start bloom', '개화 초기'), ('full bloom', '만개')], default='full bloom', max_length=50)),
                ('floriography', models.CharField(max_length=100)),
                ('flowerPhoto', models.ImageField(blank=True, null=True, upload_to='mainflower/')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=300)),
                ('deliverPrice', models.IntegerField(default=0, null=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.shop')),
            ],
        ),
        migrations.CreateModel(
            name='BunchOfFlowers',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=1000)),
                ('flowerPhoto', models.ImageField(blank=True, null=True, upload_to='bunchofflowers/')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.shop')),
            ],
        ),
    ]
