# Generated by Django 3.2.5 on 2021-07-06 00:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]