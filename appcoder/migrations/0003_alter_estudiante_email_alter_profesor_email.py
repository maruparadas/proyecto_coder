# Generated by Django 4.0.3 on 2022-03-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0002_profesor_estudiante_email_alter_estudiante_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
