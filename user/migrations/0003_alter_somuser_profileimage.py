# Generated by Django 3.2.6 on 2021-08-20 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_somuser_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='somuser',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to='mediaForm/'),
        ),
    ]