# Generated by Django 2.2.10 on 2020-04-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0005_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_image', models.ImageField(upload_to='pics')),
                ('customer_title', models.TextField()),
                ('customer_description', models.TextField()),
                ('customer_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_text', models.CharField(max_length=50)),
                ('gallery_image', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='What_we_do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_name', models.CharField(max_length=50)),
                ('what_image', models.ImageField(upload_to='pics')),
                ('what_description', models.TextField()),
            ],
        ),
    ]
