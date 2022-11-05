# Generated by Django 4.1.3 on 2022-11-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, unique=True, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Technological_operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_operations', models.CharField(max_length=50, unique=True, verbose_name='Технологическая операция')),
            ],
            options={
                'verbose_name': 'Технологическая операция',
                'verbose_name_plural': 'Технологические операции',
                'ordering': ['name_operations'],
            },
        ),
        migrations.CreateModel(
            name='Working_professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50, unique=True, verbose_name='Прфессия')),
            ],
            options={
                'verbose_name': 'Прфессия',
                'verbose_name_plural': 'Прфессии',
                'ordering': ['profession'],
            },
        ),
        migrations.CreateModel(
            name='Work_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_done', models.BooleanField(default=False, verbose_name='Готовность')),
                ('work_time', models.FloatField(blank=True, default=0, verbose_name='Время выполнения')),
                ('notes', models.TextField(blank=True, verbose_name='Примечание')),
                ('full_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='work_task.employee', to_field='full_name', verbose_name='ФИО')),
                ('name_operations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='work_task.technological_operation', to_field='name_operations', verbose_name='Прфессия')),
            ],
            options={
                'verbose_name': 'Рабочее задание',
                'verbose_name_plural': 'Рабочие задания',
                'ordering': ['name_operations'],
            },
        ),
        migrations.AddField(
            model_name='technological_operation',
            name='working_profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='work_task.working_professions', verbose_name='Прфессия'),
        ),
        migrations.AddField(
            model_name='employee',
            name='working_profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='work_task.working_professions', verbose_name='Прфессия'),
        ),
    ]
