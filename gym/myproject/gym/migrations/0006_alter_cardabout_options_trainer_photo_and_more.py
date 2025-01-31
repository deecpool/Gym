# Generated by Django 5.0.7 on 2024-10-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_alter_trainer_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardabout',
            options={'ordering': ['slug'], 'verbose_name': 'Карточку', 'verbose_name_plural': 'Карточки'},
        ),
        migrations.AddField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='is_active',
            field=models.BooleanField(choices=[(0, 'Не тренерует'), (1, 'Тренерует')], default=0, verbose_name='Тренeрует?'),
        ),
    ]
