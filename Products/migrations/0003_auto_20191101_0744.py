# Generated by Django 2.2.5 on 2019-11-01 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20191031_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
    ]