# Generated by Django 3.0 on 2021-12-14 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable('Address', 'lettings_address'),
                migrations.AlterModelTable('Letting', 'lettings_letting'),
            ],
            state_operations=[   
                migrations.RemoveField(
                    model_name='letting',
                    name='address',
                ),
                migrations.DeleteModel(
                    name='Address',
                ),
                migrations.DeleteModel(
                    name='Letting',
                ),
            ]
        )
    ]