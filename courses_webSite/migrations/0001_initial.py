# Generated by Django 4.0.1 on 2022-01-13 22:06

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
            name='categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='commentOnCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('descriptionOfRequerment', models.TextField(blank=True, max_length=500, null=True)),
                ('afterThisCourse', models.TextField(blank=True, max_length=500, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.IntegerField()),
                ('avalable', models.BooleanField(default=False)),
                ('numberOfView', models.IntegerField(default=0)),
                ('numberOfBuying', models.IntegerField(default=0)),
                ('by_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=25)),
                ('lName', models.CharField(max_length=25)),
                ('education', models.TextField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('by_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userBoughtCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.courses')),
            ],
        ),
        migrations.CreateModel(
            name='rateCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=1)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.commentoncourse')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.courses')),
            ],
        ),
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/%y')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.courses')),
            ],
        ),
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.lessons')),
            ],
        ),
        migrations.CreateModel(
            name='earnings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalFullBalunse', models.IntegerField(default=0)),
                ('avalableFullBalunse', models.IntegerField(default=0)),
                ('avalableBalunse', models.IntegerField(default=0)),
                ('userMadeCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='courseUserWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completionRate', models.IntegerField(default=0)),
                ('by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.courses')),
            ],
        ),
        migrations.AddField(
            model_name='commentoncourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_webSite.courses'),
        ),
    ]
