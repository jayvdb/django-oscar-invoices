# Generated by Django 2.1.8 on 2019-04-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscar_invoices', '0002_auto_20180822_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.CharField(max_length=128, unique=True, verbose_name='Invoice number'),
        ),
    ]
