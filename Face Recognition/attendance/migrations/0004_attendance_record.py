# Generated by Django 4.2.6 on 2023-10-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_classimage_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('roll_no', models.CharField(max_length=100)),
            ],
        ),
    ]
