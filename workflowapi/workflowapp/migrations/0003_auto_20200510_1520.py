# Generated by Django 3.0.6 on 2020-05-10 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflowapp', '0002_auto_20200510_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='steps',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='workflowapp.step'),
        ),
    ]
