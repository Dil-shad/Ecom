# Generated by Django 4.0.4 on 2022-05-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contactmodel_productmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]