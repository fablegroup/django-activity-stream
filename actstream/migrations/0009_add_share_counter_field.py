from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0008_add_click_counter_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='share_counter',
            field=models.PositiveIntegerField(default=0, db_index=True),
        ),
    ]
