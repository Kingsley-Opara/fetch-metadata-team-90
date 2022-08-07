# Generated by Django 4.0.6 on 2022-08-07 15:38

import app_data.filechecker
import app_data.models
import app_data.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import exiffield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', app_data.filechecker.ContentTypeRestrictedFileField(upload_to=app_data.models.user_directory_path, validators=[app_data.validators.validate_file_extension])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('exif', exiffield.fields.ExifField(default={}, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_file', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]