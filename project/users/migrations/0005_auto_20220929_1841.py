# Generated by Django 3.2.9 on 2022-09-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_personal_info_pro_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='e_division',
            field=models.TextField(default=1, max_length=47),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal_info',
            name='e_unit',
            field=models.TextField(default=0, max_length=47),
            preserve_default=False,
        ),
    ]
