# Generated by Django 2.2.10 on 2020-04-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0006_customer_gallery_what_we_do'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labour_name', models.CharField(max_length=50)),
                ('labour_state', models.CharField(max_length=50)),
                ('labours_city', models.CharField(max_length=50)),
                ('labours_role', models.CharField(max_length=50)),
                ('labour_salary', models.IntegerField(max_length=50)),
            ],
        ),
    ]
