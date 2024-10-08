# Generated by Django 5.1.1 on 2024-09-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_others_projects_alter_userinfo_pincode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='working_info',
            old_name='job_title',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='working_info',
            name='employer',
        ),
        migrations.AlterField(
            model_name='others',
            name='other_link',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='working_info',
            name='your_role',
            field=models.CharField(max_length=100),
        ),
    ]
