# Generated by Django 4.1.7 on 2023-03-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("magasin", "0008_remove_categorie_catégorie_produit_catégorie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorie",
            name="name",
            field=models.CharField(default="Al", max_length=50),
        ),
    ]