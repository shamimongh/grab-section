# Generated by Django 4.0.4 on 2023-04-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionselection',
            name='message',
            field=models.CharField(default='pending', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectionselection',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
