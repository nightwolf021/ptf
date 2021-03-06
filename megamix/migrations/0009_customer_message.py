# Generated by Django 3.1.2 on 2020-10-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megamix', '0008_auto_20201016_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=2048)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
