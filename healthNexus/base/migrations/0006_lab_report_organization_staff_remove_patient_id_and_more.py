# Generated by Django 4.2.3 on 2023-11-12 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_patient_doctors_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='lab_reports/')),
            ],
        ),
        migrations.CreateModel(
            name='Organization_Staff',
            fields=[
                ('staff_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='base/male_patient.png', upload_to='images/')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.organization')),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Patient_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_report_pdf', models.FileField(upload_to='patient_reports/')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.doctor')),
                ('lab_reports', models.ManyToManyField(blank=True, to='base.lab_report')),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.organization')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.patient')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.organization_staff')),
            ],
        ),
    ]
