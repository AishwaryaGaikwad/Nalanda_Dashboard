# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-17 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_exam_attempted_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_creation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=60)),
                ('exam_count', models.IntegerField()),
                ('active_exam_count', models.IntegerField()),
                ('complete_exam_count', models.IntegerField()),
            ],
        ),
    ]
