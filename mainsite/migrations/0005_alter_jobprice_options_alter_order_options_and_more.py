# Generated by Django 4.1.3 on 2022-11-21 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_alter_auto_options_alter_client_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobprice',
            options={'verbose_name': 'Цена за работу', 'verbose_name_plural': 'Цена за работы'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='second_name',
        ),
    ]
