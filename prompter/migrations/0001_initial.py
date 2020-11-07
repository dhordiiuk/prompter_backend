# Generated by Django 3.1.2 on 2020-10-17 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('description', models.TextField(blank=True)),
                ('min_time_sec', models.IntegerField(default=5)),
                ('max_time_sec', models.IntegerField(default=10)),
            ],
            options={
                'verbose_name': 'mode',
                'verbose_name_plural': 'modes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
                ('frequency', models.IntegerField(default=10)),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='prompter.mode')),
            ],
        ),
    ]