# Generated by Django 4.1.3 on 2022-11-21 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_rename_clintauto_clientauto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент'},
        ),
    ]
