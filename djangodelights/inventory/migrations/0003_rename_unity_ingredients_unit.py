# Generated by Django 4.1.5 on 2023-01-25 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_ingredients_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='unity',
            new_name='unit',
        ),
    ]