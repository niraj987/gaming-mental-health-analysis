import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")

def run_eda():
    db_path = 'd:/Web development Projects/Antig/data/gaming_health.db'
    output_dir = 'd:/Web development Projects/Antig/reports/images'
    os.makedirs(output_dir, exist_ok=True)
    
    print("Connecting to database for EDA...")
    conn = sqlite3.connect(db_path)
    
    # 1. Age distribution and avg gaming hours
    print("Querying: Average Gaming Hours by Age Group...")
    query1 = """
    SELECT 
        CASE 
            WHEN age < 18 THEN '<18'
            WHEN age BETWEEN 18 AND 24 THEN '18-24'
            WHEN age BETWEEN 25 AND 34 THEN '25-34'
            WHEN age BETWEEN 35 AND 44 THEN '35-44'
            ELSE '45+' 
        END AS age_group,
        AVG(daily_gaming_hours) as avg_gaming_hours,
        COUNT(*) as player_count
    FROM gaming_data
    GROUP BY age_group
    ORDER BY age_group
    """
    df_age = pd.read_sql(query1, conn)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_age, x='age_group', y='avg_gaming_hours', palette='viridis')
    plt.title('Average Daily Gaming Hours by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Daily Gaming Hours')
    plt.savefig(f'{output_dir}/gaming_hours_by_age.png', dpi=300)
    plt.close()
    
    # 2. Gender distribution
    print("Querying: Gender Distribution...")
    query2 = """
    SELECT gender, COUNT(*) as count
    FROM gaming_data
    GROUP BY gender
    """
    df_gender = pd.read_sql(query2, conn)
    plt.figure(figsize=(8, 8))
    plt.pie(df_gender['count'], labels=df_gender['gender'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Gender Distribution of Gamers')
    plt.savefig(f'{output_dir}/gender_distribution.png', dpi=300)
    plt.close()

    # 3. Correlation between Depression Score, Anxiety, and Gaming metrics
    # Since 10M rows correlation can be slow via python on full dataset, we sample in SQL
    print("Querying: Correlation sample for Mental Health metrics...")
    query3 = """
    SELECT daily_gaming_hours, sleep_hours, addiction_level, depression_score, anxiety_score, toxicity_exposure
    FROM gaming_data
    ORDER BY RANDOM()
    LIMIT 100000
    """
    try:
        df_corr = pd.read_sql(query3, conn)
        plt.figure(figsize=(10, 8))
        corr_matrix = df_corr.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Heatmap: Gaming & Mental Health (Sampled)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/correlation_heatmap.png', dpi=300)
        plt.close()
    except Exception as e:
        print("Note: 'toxicity_exposure' might be named differently in the dataset, let's fallback to other generic features.")
        query3_fallback = """
        SELECT daily_gaming_hours, sleep_hours, addiction_level, depression_score, anxiety_score, social_interaction_score
        FROM gaming_data
        ORDER BY RANDOM()
        LIMIT 100000
        """
        df_corr = pd.read_sql(query3_fallback, conn)
        plt.figure(figsize=(10, 8))
        corr_matrix = df_corr.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Heatmap: Gaming & Mental Health (Sampled)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/correlation_heatmap.png', dpi=300)
        plt.close()

    # 4. Addiction level vs multiplayer usage
    print("Querying: Addiction Level vs Multiplayer Ratio...")
    query4 = """
    SELECT ROUND(addiction_level) as rounded_addiction, AVG(multiplayer_ratio) as avg_multiplayer
    FROM gaming_data
    GROUP BY ROUND(addiction_level)
    ORDER BY rounded_addiction
    """
    df_addiction = pd.read_sql(query4, conn)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_addiction, x='rounded_addiction', y='avg_multiplayer', marker='o', color='crimson')
    plt.title('Average Multiplayer Ratio vs Addiction Level')
    plt.xlabel('Addiction Level')
    plt.ylabel('Average Multiplayer Ratio')
    plt.savefig(f'{output_dir}/addiction_vs_multiplayer.png', dpi=300)
    plt.close()
    
    print("EDA completed successfully. Visualizations saved to reports/images/")
    conn.close()

if __name__ == "__main__":
    run_eda()
