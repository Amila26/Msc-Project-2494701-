from pathlib import Path
import pandas as pd

from sqlalchemy import create_engine
import pymongo
from datetime import datetime, timedelta
import pymysql
import constants


HOME_DIR_ETL = f"{Path.home()}/etl_storage"

# Use if existing replace method for data loading

def load():
    transformed_todays_weather_data = pd.read_csv(f"{HOME_DIR_ETL}/transform/transformed_todays_weather_df.csv")
    # Load today's Weather Data (current weather data)
    # MySQL
    sqlEngine = create_engine('mysql+pymysql://root:12345@34.89.79.16/weather_db', pool_recycle=3306)
    dbConnection = sqlEngine.connect()
    print(transformed_todays_weather_data)
    transformed_todays_weather_data.to_sql("todays_weather_data", dbConnection, if_exists='replace', index=False)
    print("Inserted Todays data to MySQL")

    # # Load Historical Weather Data
    # # MySQL
    historical_data_last_sync_file = f"{HOME_DIR_ETL}/extract/historical_data_last_sync"
    with open(historical_data_last_sync_file, 'r') as f:
        last_sync_date_str = f.read()
    last_sync_date = datetime.strptime(last_sync_date_str, '%Y-%m-%d')
    delta = datetime.today() - last_sync_date

    if delta.days == 0 or delta.days > constants.historical_date_fetch_days_interval:
        transformed_historical_weather_data = pd.read_csv(
            f"{HOME_DIR_ETL}/transform/transformed_historical_weather_df.csv")
        print(transformed_historical_weather_data)
        transformed_historical_weather_data.to_sql("historical_weather_data", dbConnection, if_exists='replace',
                                                   index=False)
        print("Inserted Historical data to MySQL")

    

if __name__ == '__main__':
    load()
