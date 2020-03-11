# Generated by Django 3.0 on 2019-12-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191216_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='token',
            new_name='email_verification_token',
        ),
        migrations.AddField(
            model_name='user',
            name='forgot_password_token',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
