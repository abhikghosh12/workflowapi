# Generated by Django 3.0.6 on 2020-05-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='step',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='step',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
