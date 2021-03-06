# Generated by Django 4.0.5 on 2022-06-10 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='취미')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='사용자 계정')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='이메일 주소')),
                ('password', models.CharField(max_length=20, verbose_name='비밀 번호')),
                ('fullname', models.CharField(max_length=20, verbose_name='이름')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(verbose_name='소개')),
                ('birthday', models.DateField(verbose_name='생일')),
                ('age', models.IntegerField(verbose_name='나이d')),
                ('hobby', models.ManyToManyField(to='polls.hobby', verbose_name='취미')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.user', verbose_name='사용자')),
            ],
        ),
    ]
