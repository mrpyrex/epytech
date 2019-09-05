# Generated by Django 2.1.7 on 2019-09-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=1)),
                ('billing_address1', models.CharField(max_length=200)),
                ('billing_address2', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('country', models.CharField(default='Nigeria', max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('post_code', models.CharField(blank=True, max_length=200, null=True)),
                ('default', models.BooleanField(default=True)),
            ],
        ),
    ]
