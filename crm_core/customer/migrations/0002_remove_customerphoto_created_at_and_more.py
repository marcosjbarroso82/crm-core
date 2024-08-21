import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerphoto',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerphoto',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='customerphoto',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerphoto',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_by',
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='created_customers',
                to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_by',
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='updated_customers',
                to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
