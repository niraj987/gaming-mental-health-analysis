import pandas as pd
import sqlite3
import sqlalchemy
import time
def ingest_data():
    csv_file_path = 'gaming_mental_health_10M_40features.csv'
    db_path = 'sqlite:///data/gaming_health.db'
    engine = sqlalchemy.create_engine(db_path)
    chunksize = 250000
    for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):
        chunk.to_sql('gaming_data', engine, if_exists='append', index=False)
if __name__ == "__main__":
    ingest_data()