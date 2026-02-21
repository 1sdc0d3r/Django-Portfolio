# Generated for image default

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_add_image_to_hobbies_portfolio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hobbies",
            name="image",
            field=models.CharField(
                blank=True,
                default="https://img.uline.com/is/image/uline/H-11295?$LargeRHD$",
                max_length=500,
            ),
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="image",
            field=models.CharField(
                blank=True,
                default="https://img.uline.com/is/image/uline/H-11295?$LargeRHD$",
                max_length=500,
            ),
        ),
    ]
