# Generated by Django 3.0.5 on 2021-01-05 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RFID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rf_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='useraccount',
            name='otp',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='otp_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='password_reset_token',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='RFIDDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=10)),
                ('engine_no', models.CharField(max_length=255)),
                ('fuel_type', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('rf_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.RFID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PayhereDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(max_length=20)),
                ('order_id', models.CharField(max_length=20)),
                ('payhere_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('card_holder_name', models.CharField(default='', max_length=255)),
                ('card_no', models.CharField(default='', max_length=19)),
                ('card_expiry', models.CharField(default='', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
