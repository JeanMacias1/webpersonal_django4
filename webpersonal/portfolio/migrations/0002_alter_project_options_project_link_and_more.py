# Generated by Django 4.1.3 on 2023-06-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={
                "ordering": ["-created"],
                "verbose_name": "proyecto",
                "verbose_name_plural": "proyectos",
            },
        ),
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Fecha de creacion"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="imagen",
            field=models.ImageField(upload_to="projects"),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Fecha de mofificacion"
            ),
        ),
    ]
