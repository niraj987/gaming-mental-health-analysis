# 🎮 Gaming and Mental Health Analysis

Welcome to the **End-to-End Data Analysis Pipeline** for analyzing the relationship between gaming behaviors and psychological well-being. This project processes over **10 million rows** of data to provide insights into gaming habits, addiction levels, and mental health metrics.

## 🚀 Project Overview
- **Data Ingestion**: High-performance chunked ingestion into SQLite.
- **EDA**: Visualizing trends across age groups, gender, and addictive behaviors.
- **Machine Learning**: Predictive modeling using XGBoost to identify key drivers of gaming addiction.
- **Interactive Website**: A visual dashboard showcasing the final outcomes.

## 📊 Key Findings
- **Addiction Drivers**: Daily gaming hours and total screen time are the strongest predictors of addiction risk.
- **Age Trends**: Younger gamers (18-24) have the highest participation but also higher vulnerability to depressive symptoms related to gaming.
- **Social Impact**: High multiplayer ratios correlate with higher social interaction scores but also slight increases in addiction levels.

## 🛠️ How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the main analysis: `python "Project-Data Analyst.py"`
3. View outcomes in `reports/images/` or open `index.html`.

## 📂 Repository Structure
- `Project-Data Analyst.py`: Main orchestration script.
- `src/`: Modular code for ingestion, EDA, and ML.
- `docs/index.html`: Interactive visualization dashboard.
- `reports/images/`: Generated charts and visualizations.

## 🤝 Contribute / Collaborate
We welcome researchers and data analysts to contribute! Feel free to:
- Open an issue for data discrepancies.
- Submit a PR with new feature engineering ideas.
- Download the dataset to run your own experiments.

*Built with ❤️ by Niraj Kumar.*