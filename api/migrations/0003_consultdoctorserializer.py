# Generated by Django 2.2.6 on 2019-11-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_consultdoctor_questionserializer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultDoctorSerializer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]