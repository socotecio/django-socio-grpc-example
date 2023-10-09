# Generated by Django 4.2.2 on 2023-10-07 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("author_id", models.UUIDField(primary_key=True, serialize=False)),
                ("name_first", models.CharField(max_length=100)),
                ("name_last", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="PublicationCategory",
            fields=[
                ("category_id", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                ("publisher_id", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state_province", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("website", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Journal",
            fields=[
                ("journal_id", models.UUIDField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("publication_date", models.DateField()),
                ("volume", models.IntegerField()),
                ("issue", models.IntegerField()),
                ("issn", models.CharField(max_length=20)),
                ("authors", models.ManyToManyField(to="async_example_bib_app.author")),
                (
                    "categories",
                    models.ManyToManyField(to="async_example_bib_app.publicationcategory"),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="async_example_bib_app.publisher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("book_id", models.UUIDField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("isbn", models.CharField(max_length=20)),
                ("publication_date", models.DateField()),
                ("authors", models.ManyToManyField(to="async_example_bib_app.author")),
                (
                    "categories",
                    models.ManyToManyField(to="async_example_bib_app.publicationcategory"),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="async_example_bib_app.publisher",
                    ),
                ),
            ],
        ),
    ]