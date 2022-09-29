# Generated by Django 4.1.1 on 2022-09-27 00:46

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings



class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
