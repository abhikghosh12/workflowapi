# Generated by Django 3.0.6 on 2020-05-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0011_auto_20200511_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='steps',
            field=models.ManyToManyField(blank=True, to='workflowapp.step'),
        ),
    ]
