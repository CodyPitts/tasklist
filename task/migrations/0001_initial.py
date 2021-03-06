# Generated by Django 2.2.6 on 2019-10-08 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usergroup', '0001_initial'),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('time_estimate', models.CharField(blank=True, max_length=20)),
                ('groups', models.ManyToManyField(blank=True, to='usergroup.UserGroup')),
                ('users', models.ManyToManyField(blank=True, to='userprofile.UserProfile')),
            ],
        ),
    ]
