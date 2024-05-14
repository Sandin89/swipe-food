from flask import current_app
import pandas as pd
import click
from .models import db, Recipe
from googletrans import Translator
import shutil
import os

translator = Translator()

@click.command("init-db")
def init_db():
    with current_app.app_context():
        db.drop_all()
        db.create_all()

        csv_file = os.path.join("archive", "Food Ingredients and Recipe Dataset with Image Name Mapping.csv")
        df = pd.read_csv(csv_file)
        df = df.dropna()
        df = df.head(100)

        destination_directory = os.path.join(current_app.static_folder, 'images')
        os.makedirs(destination_directory, exist_ok=True)

        for image_name in df["Image_Name"]:
            source_file = os.path.join("archive", "Food Images", image_name)
            destination_file = os.path.join(destination_directory, image_name)
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied {source_file} to {destination_file}")
            except Exception as e:
                print(f"Failed to copy {source_file}: {e}")

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
