# Generated by Django 5.0.3 on 2024-04-14 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_delete_transactionsmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'LoadPaid'), (5, 'Transformed'), (6, 'Received')], null=True),
        ),
    ]
