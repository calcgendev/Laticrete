# Generated by Django 3.0.2 on 2020-07-15 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laticreteapp', '0005_auto_20200715_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='details',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
