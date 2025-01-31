# Generated by Django 1.9.13 on 2021-08-26 19:20
import uuid

from django.db import migrations, models
from django.contrib.postgres.operations import (
    AddIndexConcurrently,
    RemoveIndexConcurrently,
)


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("actstream", "0006_remove_uuid_null"),
    ]

    operations = [
        AddIndexConcurrently(
            model_name="action",
            index=models.Index(
                fields=["actor_object_id"],
                condition=models.Q(deleted=False),
                name="actstream_action_actor_obj_idx",
            ),
        ),
        AddIndexConcurrently(
            model_name="action",
            index=models.Index(
                fields=["action_object_object_id", "action_object_content_type_id"],
                name="actstre_act_objid_typeid_idx",
            ),
        ),
        AddIndexConcurrently(
            model_name="action",
            index=models.Index(
                fields=["target_object_id", "target_content_type_id"],
                name="actstre_act_trgtid_typeid_idx",
            ),
        ),
    ]
