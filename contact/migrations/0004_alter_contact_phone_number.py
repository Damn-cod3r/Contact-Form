# Generated by Django 5.0.7 on 2024-07-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_submitted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
