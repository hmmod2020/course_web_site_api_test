# Generated by Django 4.0.1 on 2022-03-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_webSite', '0011_alter_userboughtcourse_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='create_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transactionType',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
