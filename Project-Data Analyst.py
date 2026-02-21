import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ingest_db import ingest_data
from src.eda_analysis import run_eda
from src.ml_model import run_ml_pipeline

def main():
    print(" Project: Data Analyst - Gaming & Mental Health Pipeline")
    run_eda()
    run_ml_pipeline()
    print("All tasks completed successfully!")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()