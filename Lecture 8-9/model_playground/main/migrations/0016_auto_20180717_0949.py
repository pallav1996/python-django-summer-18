# Generated by Django 2.0.4 on 2018-07-17 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_person_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('HOD', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.Subject'),
        ),
    ]
