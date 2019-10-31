# Generated by Django 2.2.5 on 2019-10-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('0', 'Out Stock'), ('1', 'In Stock'), ('2', 'Running Low')], default=1, max_length=1),
        ),
    ]