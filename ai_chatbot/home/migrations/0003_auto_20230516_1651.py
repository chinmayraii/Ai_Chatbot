# Generated by Django 2.2.28 on 2023-05-16 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_rename_user_id_bot_user_chatbot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mob', models.IntegerField(blank=True, unique=True)),
                ('user_address', models.TextField()),
                ('user_img', models.ImageField(upload_to='images')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
