# Generated by Django 4.1.5 on 2023-02-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_sheba_featureservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheba',
            name='servicecategory',
            field=models.CharField(choices=[('service1', 'IT Service'), ('service2', 'Cleaning Service'), ('service3', 'Electric & Plumbing Service'), ('service4', 'others')], default='service1', max_length=100),
        ),
    ]
