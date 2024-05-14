from flask import current_app
import pandas as pd
import click
from .models import db, Recipe
from googletrans import Translator
import shutil

translator = Translator()


def get_db():
    return db.engine.connect()


@click.command("init-db")
def init_db():
    with current_app.app_context():
        db.drop_all()
        db.create_all()

        csv_file = "archive\Food Ingredients and Recipe Dataset with Image Name Mapping.csv"
        df = pd.read_csv(csv_file)
        df = df.dropna()
        df = df.head(100)
        
        for image_name in df["Image_Name"]:
            source_file = "swiper/static/Food Images" + image_name + ".jpg"
            destination_directory = "static/images"
            shutil.copy(source_file, destination_directory)

        for index, row in df.iterrows():
            recipe = Recipe(
                title=row["Title"],
                ingredients=row["Ingredients"],
                instructions=row["Instructions"],
                image_name=row["Image_Name"],
                cleaned_ingredients=row["Cleaned_Ingredients"],
            )

            db.session.add(recipe)

        db.session.commit()
        print("Database initialization successful.")


def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db)
