# Generated by Django 3.0.2 on 2020-04-03 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applicationVideos',
            fields=[
                ('fileName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('videoFile', models.FileField(upload_to='static/')),
            ],
            options={
                'verbose_name': 'Application Video',
                'verbose_name_plural': 'Application Videos',
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('imageName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='static/')),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousels',
            },
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('fileName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('pdfFile', models.FileField(upload_to='static/')),
            ],
            options={
                'verbose_name': 'Download',
                'verbose_name_plural': 'Downloads',
            },
        ),
        migrations.CreateModel(
            name='feedBacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30, null=True)),
                ('lastName', models.CharField(max_length=30, null=True)),
                ('company', models.CharField(max_length=40, null=True)),
                ('postalCode', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=30, null=True)),
                ('typeOfAssistance', models.CharField(max_length=1000, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='groutColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorName', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(upload_to='static/')),
            ],
            options={
                'verbose_name': 'Grout Color',
                'verbose_name_plural': 'Grout Colors',
            },
        ),
        migrations.CreateModel(
            name='lineCategory',
            fields=[
                ('categoryName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='static/')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='pastProjects',
            fields=[
                ('projectTitle', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('details', models.CharField(max_length=10000, null=True)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'verbose_name': 'Past Project',
                'verbose_name_plural': 'Past Projects',
            },
        ),
        migrations.CreateModel(
            name='productLine',
            fields=[
                ('lineName', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Product Line',
                'verbose_name_plural': 'Product Lines',
            },
        ),
        migrations.CreateModel(
            name='solutionCategory',
            fields=[
                ('categoryName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='static/')),
            ],
            options={
                'verbose_name': 'Solution Category',
                'verbose_name_plural': 'Solution Categories',
            },
        ),
        migrations.CreateModel(
            name='solutionLine',
            fields=[
                ('lineName', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Solution Line',
                'verbose_name_plural': 'Solution Lines',
            },
        ),
        migrations.CreateModel(
            name='tileColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorName', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(upload_to='static/')),
            ],
            options={
                'verbose_name': 'Tile Color',
                'verbose_name_plural': 'Tile Colors',
            },
        ),
        migrations.CreateModel(
            name='whereToBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('storeName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('postalCode', models.CharField(max_length=40)),
                ('telephone', models.CharField(max_length=15)),
                ('faxNumber', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Where to buy',
                'verbose_name_plural': 'Where to buy',
            },
        ),
        migrations.CreateModel(
            name='solutionD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solutionName', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('details', models.CharField(max_length=10000, null=True)),
                ('categoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laticreteapp.solutionCategory')),
            ],
            options={
                'verbose_name': 'Solution',
                'verbose_name_plural': 'Solutions',
            },
        ),
        migrations.AddField(
            model_name='solutioncategory',
            name='lineName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laticreteapp.solutionLine'),
        ),
        migrations.CreateModel(
            name='productD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('details', models.CharField(max_length=10000, null=True)),
                ('categoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laticreteapp.lineCategory')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='linecategory',
            name='lineName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laticreteapp.productLine'),
        ),
    ]
