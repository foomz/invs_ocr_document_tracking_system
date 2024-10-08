# Generated by Django 4.2.14 on 2024-08-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0011_alter_finalreport_date_received'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_no', models.CharField(default='', max_length=255)),
                ('adinvs_rs', models.CharField(default='', max_length=255)),
                ('reference_no', models.CharField(blank=True, max_length=100, null=True)),
                ('rdo', models.CharField(max_length=255)),
                ('requesting_party_aoc', models.CharField(max_length=255)),
                ('mode_of_opn', models.CharField(max_length=255)),
                ('noc', models.CharField(max_length=255)),
                ('complainant', models.CharField(max_length=255)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_opn', models.DateField(blank=True, null=True)),
                ('place_of_opn', models.CharField(blank=True, max_length=100, null=True)),
                ('approve_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('estimated_exp', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeOfOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_no', models.CharField(default='', max_length=255)),
                ('adinvs_rs', models.CharField(default='', max_length=255)),
                ('reference_no', models.CharField(blank=True, max_length=100, null=True)),
                ('rdo', models.CharField(max_length=255)),
                ('requesting_party_aoc', models.CharField(max_length=255)),
                ('mode_of_opn', models.CharField(max_length=255)),
                ('noc', models.CharField(max_length=255)),
                ('complainant', models.CharField(max_length=255)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_opn', models.DateField(blank=True, null=True)),
                ('place_of_opn', models.CharField(blank=True, max_length=100, null=True)),
                ('approve_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('estimated_exp', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_no', models.CharField(default='', max_length=255)),
                ('adinvs_rs', models.CharField(default='', max_length=255)),
                ('reference_no', models.CharField(blank=True, max_length=100, null=True)),
                ('rdo', models.CharField(max_length=255)),
                ('requesting_party_aoc', models.CharField(max_length=255)),
                ('mode_of_opn', models.CharField(max_length=255)),
                ('noc', models.CharField(max_length=255)),
                ('complainant', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('date_of_opn', models.DateField(blank=True, null=True)),
                ('place_of_opn', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostOperationReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_no', models.CharField(default='', max_length=255)),
                ('adinvs_rs', models.CharField(default='', max_length=255)),
                ('reference_no', models.CharField(blank=True, max_length=100, null=True)),
                ('rdo', models.CharField(max_length=255)),
                ('requesting_party_aoc', models.CharField(max_length=255)),
                ('mode_of_opn', models.CharField(max_length=255)),
                ('noc', models.CharField(max_length=255)),
                ('complainant', models.CharField(max_length=255)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_opn', models.DateField(blank=True, null=True)),
                ('place_of_opn', models.CharField(blank=True, max_length=100, null=True)),
                ('approve_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('estimated_exp', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
