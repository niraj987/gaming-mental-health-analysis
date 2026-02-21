import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os
def run_eda():
    db_path = 'data/gaming_health.db'
    conn = sqlite3.connect(db_path)
    query = "SELECT age, daily_gaming_hours FROM gaming_data LIMIT 10000"
    df = pd.read_sql(query, conn)
    print("EDA Done")
    conn.close()