# Generated by Django 3.1.5 on 2021-02-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_auto_20210204_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gmail', models.EmailField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
