# Generated by Django 4.0 on 2021-12-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
