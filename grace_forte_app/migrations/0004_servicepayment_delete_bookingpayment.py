# Generated by Django 5.0.2 on 2024-03-14 13:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grace_forte_app', '0003_trainingpayment_isapproved'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePayment',
            fields=[
                ('Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('paymentStatus', models.CharField(default='Pending', max_length=50)),
                ('proofBase', models.TextField()),
                ('bookedDuration', models.CharField(default='1hr', max_length=50)),
                ('expectedAmount', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('isApproved', models.BooleanField(default=False)),
                ('approvedDate', models.DateTimeField(blank=True, null=True)),
                ('preferedBookingDate', models.DateTimeField(blank=True, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateDeleted', models.DateTimeField(blank=True, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_service', to='grace_forte_app.accountinformation')),
                ('approvedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_admin_approved', to=settings.AUTH_USER_MODEL)),
                ('isDeletedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_payment', to='grace_forte_app.servicerendered')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_service', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ServicePayment',
            },
        ),
        migrations.DeleteModel(
            name='BookingPayment',
        ),
    ]
