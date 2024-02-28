# Generated by Django 3.2.17 on 2023-03-15 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0009_cart_is_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='razor_pay_order_id',
            new_name='razorpay_order_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='razor_pay_payment_id',
            new_name='razorpay_payment_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='razor_pay_payment_signature',
            new_name='razorpay_payment_signature',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]