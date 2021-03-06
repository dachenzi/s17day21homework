# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 06:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('summary', models.CharField(max_length=255, verbose_name='简介')),
                ('com_form', models.CharField(max_length=255, verbose_name='来自')),
                ('head', models.CharField(max_length=255, verbose_name='头像')),
                ('like_count', models.IntegerField(default=0, verbose_name='点赞数')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='NewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=16, verbose_name='新闻类型')),
                ('description', models.CharField(max_length=255, verbose_name='新闻描述')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='账号')),
                ('mbpwd', models.CharField(max_length=12, verbose_name='密码')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='like',
            field=models.ManyToManyField(through='app01.Like', to='app01.UserInfo', verbose_name='点赞'),
        ),
        migrations.AddField(
            model_name='news',
            name='newscategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.NewType', verbose_name='新闻类型'),
        ),
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='app01.UserInfo', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='like',
            name='nid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsid', to='app01.News'),
        ),
        migrations.AddField(
            model_name='like',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.News', verbose_name='评论的新闻ID'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserInfo', verbose_name='评论作者'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('nid', 'uid')]),
        ),
    ]
