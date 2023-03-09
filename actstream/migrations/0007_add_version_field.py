from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0006_remove_uuid_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='version',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
