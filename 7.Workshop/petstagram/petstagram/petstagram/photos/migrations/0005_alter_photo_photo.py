# Generated by Django 4.1.1 on 2022-10-19 16:32

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='pet_photos/', validators=[petstagram.photos.validators.validate_file_less_than_5mb]),
        ),
    ]