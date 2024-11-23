# Generated by Django 4.2.16 on 2024-11-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('sport', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('предстоящий', 'Предстоящий'), ('идет', 'Идет'), ('завершен', 'Завершен')], max_length=50)),
            ],
        ),
    ]