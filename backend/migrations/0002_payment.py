# Generated by Django 5.2.4 on 2025-07-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(max_length=12)),
                ('checkoutrequestid', models.CharField(unique=True)),
                ('amountpaid', models.IntegerField()),
            ],
        ),
    ]
