# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 01:57
from __future__ import unicode_literals

import answerdiff_dev.models
import datetime
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
            name='AcceptedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0)),
                ('tries', models.IntegerField(default=0)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment_message', models.CharField(default=b'', max_length=255)),
                ('comment_is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(default=b'', max_length=255, unique=True)),
                ('contest_description', models.TextField(blank=True, default=b'')),
                ('contest_rules', models.TextField(default=b'')),
                ('contest_start_time', models.DateTimeField()),
                ('contest_end_time', models.DateTimeField()),
                ('contest_consecutive_submission_halt_time', models.DurationField(default=datetime.timedelta(0, 30))),
                ('contest_number_of_level', models.PositiveIntegerField()),
                ('contest_questions_in_each_level', models.PositiveIntegerField()),
                ('contest_user_level_increment_type', models.CharField(choices=[(b'TYPE1', b'TYPE1'), (b'TYPE2', b'TYPE2')], max_length=6)),
                ('contest_number_to_increment_level_at', models.PositiveIntegerField()),
                ('contest_question_type', models.CharField(choices=[(b'FL', b'File'), (b'ST', b'String')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_compile_arguments', models.CharField(blank=True, default=b'', max_length=255)),
                ('language_runtime_arguments', models.CharField(blank=True, default=b'', max_length=255)),
                ('language_file_extension', models.CharField(default=b'', max_length=16, unique=True)),
                ('language_is_preprocessed', models.BooleanField(default=False)),
                ('language_is_sandboxed', models.BooleanField(default=False)),
                ('language_is_compiled', models.BooleanField(default=False)),
                ('language_is_checked', models.BooleanField(default=False)),
                ('language_is_executed', models.BooleanField(default=False)),
                ('language_name', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nick', models.CharField(max_length=255)),
                ('user_last_ip', models.GenericIPAddressField(default=b'0.0.0.0')),
                ('user_access_level', models.PositiveIntegerField(default=1)),
                ('user_score', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_level', models.IntegerField()),
                ('question_number', models.IntegerField()),
                ('question_title', models.CharField(max_length=255, unique=True)),
                ('question_desc', models.TextField()),
                ('question_image', models.ImageField(blank=True, upload_to=answerdiff_dev.models.question_image_filepath)),
                ('question_upload_type', models.CharField(choices=[(b'FL', b'File'), (b'ST', b'String')], default=b'ST', max_length=2)),
                ('question_answer_string', models.CharField(blank=True, default=b'', max_length=255)),
                ('question_upload_file', models.FileField(blank=True, upload_to=answerdiff_dev.models.question_input_file_upload)),
                ('question_gold_upload_file', models.FileField(blank=True, upload_to=answerdiff_dev.models.question_gold_file_upload)),
                ('question_checker_script', models.FileField(blank=True, upload_to=answerdiff_dev.models.question_checker_upload)),
                ('question_preprocess_script', models.FileField(blank=True, upload_to=answerdiff_dev.models.question_preprocess_upload)),
                ('question_time_limit', models.CharField(blank=True, default=b'', max_length=16)),
                ('question_memory_limit', models.CharField(blank=True, default=b'', max_length=16)),
                ('question_output_limit', models.CharField(blank=True, default=b'', max_length=16)),
                ('question_restrict_language_to', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='answerdiff_dev.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_timestamp', models.DateTimeField(auto_now_add=True)),
                ('submission_string', models.CharField(blank=True, default=b'', max_length=255)),
                ('submission_storage', models.FileField(blank=True, upload_to=answerdiff_dev.models.submission_storage_path)),
                ('submission_state', models.CharField(choices=[(b'WA', b'Wrong Answer'), (b'AC', b'Accepted'), (b'PR', b'Processing')], default=b'PR', max_length=2)),
                ('submission_score', models.FloatField(default=0)),
                ('submission_runtime_log', models.CharField(blank=True, default=b'', max_length=255)),
                ('submission_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answerdiff_dev.Question')),
                ('submission_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answerdiff_dev.Question'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='acceptedquestion',
            name='record_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answerdiff_dev.Question'),
        ),
        migrations.AddField(
            model_name='acceptedquestion',
            name='record_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]