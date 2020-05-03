from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_model', 'ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_model',
            name='extra_data',
            field=models.TextField(null=True, verbose_name='extra data', blank=True),
        ),
    ]
