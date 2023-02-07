# Generated by Django 4.1.6 on 2023-02-05 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('is_active', models.BooleanField(default=True)),
                ('ratingAuthor', models.SmallIntegerField(default=0)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('categoryPost', models.CharField(choices=[('News', 'Новость'), ('Article', 'Статья')], default='Article', max_length=100)),
                ('dateCreate', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='Фото')),
                ('slug', models.SlugField(max_length=100)),
                ('rating', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['dateCreate', 'title'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.category')),
                ('postTrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='newsapp.PostCategory', to='newsapp.category', verbose_name='Категория'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('commentCreate', models.DateTimeField(auto_now_add=True)),
                ('raiting', models.SmallIntegerField(default=0)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsapp.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]