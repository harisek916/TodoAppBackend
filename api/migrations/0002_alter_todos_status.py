# Generated by Django 5.0.6 on 2024-05-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('inprogress', 'inprogress'), ('completed', 'completed')], default='pending', max_length=200),
        ),
    ]