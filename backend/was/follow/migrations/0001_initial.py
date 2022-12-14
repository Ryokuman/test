# Generated by Django 4.0.6 on 2022-10-15 08:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='follow',
            fields=[
                ('follow_pk', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to='users.user')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='users.user')),
            ],
            options={
                'db_table': 'follow',
            },
        ),
    ]
