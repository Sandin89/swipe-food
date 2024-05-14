import pandas as pd
import shutil

food_csv_db = pd.read_csv('static\databas\Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

food_csv_db = food_csv_db.dropna()
food_csv_db = food_csv_db.rename(columns={'Unnamed: 0': 'num'})
food_csv_db = food_csv_db.head(100)

food_csv_db.to_csv('.\static\databas\Food_db.csv')


food_csv_db.to_parquet('.\static\databas\Food_db.parquet')


food_parquet_db = pd.read_parquet('static\databas\Food_db.parquet')

for image_name in food_parquet_db['Image_Name']:

    source_file = 'static/databas/Food Images/Food Images/'+image_name+'.jpg'
    destination_directory = 'static/databas/food_images'

    shutil.copy(source_file, destination_directory)

