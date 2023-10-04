from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20211218_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='date_posted',
            new_name='time_created',
        ),
    ]