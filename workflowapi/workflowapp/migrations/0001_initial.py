# Generated by Django 2.2.3 on 2020-05-14 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('text', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('workflow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='workflowapp.workflow')),
            ],
        ),
    ]
