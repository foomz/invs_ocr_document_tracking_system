# Generated by Django 4.2.14 on 2024-08-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_image_alter_document_date_transmitted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutgoingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_no', models.CharField(max_length=100)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('received_from', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_document', models.CharField(blank=True, max_length=255, null=True)),
                ('subjects', models.TextField(blank=True, null=True)),
                ('forwarded_to', models.CharField(blank=True, max_length=255, null=True)),
                ('date_transmitted', models.DateField(blank=True, null=True)),
                ('received_by', models.CharField(blank=True, max_length=255, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('reference_no', models.CharField(blank=True, max_length=100, null=True)),
                ('encoded_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
