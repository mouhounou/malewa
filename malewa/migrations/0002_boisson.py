# Generated by Django 5.0.6 on 2024-06-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malewa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='boisson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=4)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bImage', models.URLField()),
            ],
        ),
    ]
