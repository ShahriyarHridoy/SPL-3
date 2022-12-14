# Generated by Django 3.2.9 on 2022-09-27 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(unique=True)),
                ('employee_name', models.TextField(max_length=47)),
                ('email', models.EmailField(max_length=20)),
                ('father_name', models.TextField(max_length=255)),
                ('mother_name', models.DateTimeField(auto_now_add=True)),
                ('birth_date', models.DateField()),
                ('home_district', models.TextField(max_length=255)),
                ('gender', models.TextField(max_length=50)),
                ('religion', models.TextField(max_length=255)),
                ('national_ID', models.IntegerField()),
                ('passport', models.TextField(max_length=255)),
                ('driving_licence', models.TextField(max_length=50)),
                ('gpf_cpf', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('blood_group', models.TextField(max_length=3)),
                ('marital_status', models.TextField(max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
