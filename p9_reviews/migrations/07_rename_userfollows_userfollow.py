from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0006_userfollows'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFollows',
            new_name='UserFollow',
        ),
    ]