# Generated by Django 4.0.2 on 2022-02-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_questionanswer_timesasked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='timesAsked',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]