# Generated manually to remove payment fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_appointment_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='consultation_fee',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='is_paid',
        ),
    ]
