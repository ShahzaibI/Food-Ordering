# Generated by Django 5.1.5 on 2025-01-30 05:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_slug', models.SlugField(max_length=255, unique=True)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField(default=0)),
                ('product_demo_price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('prodict_images', models.ImageField(upload_to='products/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductMetaInformation',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_measuring', models.CharField(blank=True, choices=[('kg', 'kg'), ('ML', 'ML'), ('l', 'l'), ('ml', 'ml'), (None, None)], max_length=100, null=True)),
                ('product_quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('is_restrict', models.BooleanField(default=False)),
                ('restrict_quantity', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='meta_info', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
