# Generated by Django 4.2.14 on 2024-08-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0015_remove_noticeofoperation_approve_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityToOperate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=500)),
                ('month', models.CharField(max_length=500)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
