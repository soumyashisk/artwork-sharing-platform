# Generated by Django 5.1.2 on 2024-11-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/profile-pic-placeholder.png', upload_to='uploads/profile_pics/'),
        ),
    ]