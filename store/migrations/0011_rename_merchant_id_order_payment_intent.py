# Generated by Django 4.2.1 on 2023-05-28 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merchant_id',
            new_name='payment_intent',
        ),
    ]