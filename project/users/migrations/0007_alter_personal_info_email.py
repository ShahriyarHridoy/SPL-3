# Generated by Django 3.2.9 on 2022-09-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_personal_info_pro_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
