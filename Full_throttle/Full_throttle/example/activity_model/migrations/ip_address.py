from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_model', 'initial_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_model',
            name='ip_address',
            field=models.GenericIPAddressField(null=True, verbose_name='user IP', blank=True),
        ),
    ]

