# Generated by Django 4.1.2 on 2022-11-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommanage', '0006_alter_classroom_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]