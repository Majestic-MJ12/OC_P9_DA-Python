from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_rename_userfollows_userfollow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFollow',
        ),
    ]