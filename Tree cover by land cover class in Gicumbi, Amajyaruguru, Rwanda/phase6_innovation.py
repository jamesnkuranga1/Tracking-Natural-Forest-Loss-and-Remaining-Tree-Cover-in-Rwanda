# Phase 6: Innovation – Visual Trends and Forest Change Insights

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load evaluated data
df = pd.read_csv("gicumbi_evaluation_results.csv")

# 2. Check columns
required_cols = ['year', 'Cluster', 'Forest_Area_ha']
if not all(col in df.columns for col in required_cols):
    print("Required columns not found. Please ensure 'year', 'Cluster', and 'Forest_Area_ha' exist.")
else:
    # 3. Forest area trend over time per cluster
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='year', y='Forest_Area_ha', hue='Cluster', palette='tab10')
    plt.title("Forest Area Trends Over Time by Cluster")
    plt.xlabel("Year")
    plt.ylabel("Forest Area (ha)")
    plt.grid(True)
    plt.legend(title='Cluster')
    plt.tight_layout()
    plt.show()

    # 4. Pivot table for heatmap
    heatmap_data = df.pivot_table(index='adm2', columns='year', values='Forest_Area_ha', aggfunc='sum')
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=0.5, annot=True, fmt=".0f")
    plt.title("Heatmap of Forest Area Distribution by Year and Sector")
    plt.xlabel("Year")
    plt.ylabel("Sector (adm2)")
    plt.tight_layout()
    plt.show()

    # 5. Identify years with largest changes (loss or gain)
    change_by_year = df.groupby('year')['Forest_Area_ha'].sum().diff().fillna(0)
    most_loss_year = change_by_year.idxmin()
    most_gain_year = change_by_year.idxmax()

    print(f"\nYear with largest forest LOSS: {most_loss_year} ({change_by_year[most_loss_year]:.2f} ha)")
    print(f"Year with largest forest GAIN: {most_gain_year} (+{change_by_year[most_gain_year]:.2f} ha)")

    # 6. Save innovation insights
    change_by_year_df = change_by_year.reset_index().rename(columns={'Forest_Area_ha': 'Annual_Change_ha'})
    change_by_year_df.to_csv("gicumbi_forest_change_trends.csv", index=False)
    print("Innovation results saved to 'gicumbi_forest_change_trends.csv'.")
