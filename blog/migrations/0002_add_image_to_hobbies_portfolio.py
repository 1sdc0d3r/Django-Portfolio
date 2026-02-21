# Generated manually for image fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobbies',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
