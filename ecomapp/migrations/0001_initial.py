# Generated by Django 3.2.7 on 2021-10-27 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_name', models.CharField(max_length=30)),
                ('adm_email', models.EmailField(max_length=254)),
                ('adm_password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_name', models.CharField(max_length=30)),
                ('usr_id', models.CharField(max_length=30)),
                ('usr_email', models.CharField(max_length=30)),
                ('usr_contact', models.CharField(max_length=30)),
                ('feedback', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=30)),
                ('item_price', models.CharField(max_length=30)),
                ('item_id', models.CharField(max_length=30)),
                ('usr_name', models.CharField(max_length=30)),
                ('usr_id', models.CharField(max_length=30)),
                ('usr_email', models.CharField(max_length=30)),
                ('usr_contact', models.CharField(max_length=30)),
                ('order_status', models.CharField(max_length=30)),
                ('purchase_date', models.CharField(max_length=30)),
                ('delivery_date', models.CharField(max_length=30)),
                ('mode_of_payment', models.CharField(max_length=30)),
                ('shipping_address', models.CharField(max_length=30)),
                ('order_code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('item_category', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=30)),
                ('item_price', models.CharField(max_length=30)),
                ('item_price_discount', models.CharField(max_length=30)),
                ('item_comment', models.CharField(max_length=30)),
                ('item_description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=30)),
                ('item_price', models.CharField(max_length=30)),
                ('item_quantity', models.CharField(max_length=30)),
                ('usr_name', models.CharField(max_length=30)),
                ('usr_id', models.CharField(max_length=30)),
                ('usr_email', models.CharField(max_length=30)),
                ('usr_contact', models.CharField(max_length=30)),
                ('purchase_date', models.CharField(max_length=30)),
                ('delivery_date', models.CharField(max_length=30)),
                ('mode_of_payment', models.CharField(max_length=30)),
                ('shipping_address', models.CharField(max_length=30)),
                ('order_code', models.CharField(max_length=30)),
                ('order_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('usr_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('usr_name', models.CharField(max_length=30)),
                ('usr_email', models.EmailField(max_length=254)),
                ('usr_password', models.CharField(max_length=12)),
                ('usr_address', models.CharField(max_length=12)),
                ('usr_contact', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.items')),
                ('c_usr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.useraccount')),
            ],
        ),
    ]
