# Generated by Django 4.2.3 on 2023-07-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_cancelledtickets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancelledtickets',
            old_name='booking_date_time',
            new_name='cancelled_date_time',
        ),
        migrations.RemoveField(
            model_name='cancelledtickets',
            name='age',
        ),
        migrations.RemoveField(
            model_name='cancelledtickets',
            name='fare_charges',
        ),
        migrations.RemoveField(
            model_name='cancelledtickets',
            name='p_mail',
        ),
        migrations.RemoveField(
            model_name='cancelledtickets',
            name='p_phone',
        ),
        migrations.RemoveField(
            model_name='cancelledtickets',
            name='sex',
        ),
        migrations.AlterField(
            model_name='cancelledtickets',
            name='status',
            field=models.CharField(default='CANCELLED', max_length=20),
        ),
    ]