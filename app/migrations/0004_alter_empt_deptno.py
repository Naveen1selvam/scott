# Generated by Django 4.1.7 on 2023-04-07 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_empt_commission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empt',
            name='DeptNo',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='app.depat'),
        ),
    ]
