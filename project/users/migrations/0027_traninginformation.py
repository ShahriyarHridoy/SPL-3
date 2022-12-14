# Generated by Django 3.2.9 on 2022-10-17 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0026_auto_20221013_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraningInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traning_type', models.TextField(max_length=150)),
                ('traning_title', models.TextField(max_length=300)),
                ('traning_institution', models.TextField(max_length=200)),
                ('traning_country', models.TextField(max_length=150)),
                ('traning_start_date', models.DateField()),
                ('traning_end_date', models.DateField()),
                ('traning_grade', models.IntegerField()),
                ('traning_position', models.TextField(max_length=150)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
