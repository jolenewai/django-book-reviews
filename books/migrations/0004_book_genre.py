# Generated by Django 2.2.6 on 2020-05-05 08:56

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.fields.CharField, to='books.Genre'),
            preserve_default=False,
        ),
    ]
