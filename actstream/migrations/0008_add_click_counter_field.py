from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0007_add_version_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='click_counter',
            field=models.PositiveIntegerField(default=0, db_index=True),
        ),
    ]
