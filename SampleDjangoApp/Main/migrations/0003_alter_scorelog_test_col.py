# Generated by Django 4.1 on 2022-11-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_scorelog_test_col'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorelog',
            name='test_col',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]