import pandas as pd
import sqlite3
import sqlalchemy
import time

def ingest_data():
    csv_file_path = 'd:/Web development Projects/project/gaming_mental_health_10M_40features.csv'
    db_path = 'sqlite:///d:/Web development Projects/project/data/gaming_health.db'
    
    print(f"Connecting to database: {db_path}")
    engine = sqlalchemy.create_engine(db_path)
    
    chunksize = 250000 
    table_name = 'gaming_data'
    
    print(f"Starting ingestion for {csv_file_path} in chunks of {chunksize}...")
    start_time = time.time()
    
    chunk_no = 1
    for chunk in pd.read_csv(csv_file_path, chunksize=chunksize):
        # Insert into the database
        chunk.to_sql(table_name, engine, if_exists='append' if chunk_no > 1 else 'replace', index=False)
        print(f"[{chunk_no}] Uploaded chunk {chunk_no}.")
        chunk_no += 1
        
    end_time = time.time()
    print(f"Finished ingesting data in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    ingest_data()
