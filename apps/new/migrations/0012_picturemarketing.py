# Generated by Django 5.2 on 2025-04-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0011_awardnumber_title_participantnumbers_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureMarketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon_class', models.CharField(max_length=100)),
            ],
        ),
    ]
