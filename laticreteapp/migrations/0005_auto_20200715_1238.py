# Generated by Django 3.0.2 on 2020-07-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laticreteapp', '0004_auto_20200715_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='pdfFile',
            field=models.FileField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='videoFile',
            field=models.FileField(blank=True, null=True, upload_to='static/'),
        ),
    ]