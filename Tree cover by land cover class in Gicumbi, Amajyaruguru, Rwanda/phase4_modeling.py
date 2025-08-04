# Phase 4: Modeling – Understanding and Interpreting Clusters

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load clustered dataset
df = pd.read_csv("gicumbi_clustered.csv")

# 2. Rename columns for readability (optional)
df.rename(columns={
    'wri_tropical_tree_cover_extent__ha': 'Forest_Area_ha'
}, inplace=True)

# 3. Analyze distribution of clusters
cluster_counts = df['Cluster'].value_counts().sort_index()
print("Number of records per cluster:")
print(cluster_counts)

# 4. Summary stats by cluster
cluster_summary = df.groupby('Cluster')['Forest_Area_ha'].agg(['mean', 'min', 'max', 'median', 'std'])
print("\nForest Area stats per Cluster:")
print(cluster_summary)

# 5. Visualization: Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Cluster', y='Forest_Area_ha', palette='Set2')
plt.title("Distribution of Forest Area per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Forest Area (ha)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Optional: Pie chart to show proportion of records per cluster
plt.figure(figsize=(6, 6))
plt.pie(cluster_counts, labels=cluster_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Proportion of Records per Cluster")
plt.show()

# 7. Save cluster summary to CSV
cluster_summary.to_csv("cluster_summary_gicumbi.csv")
print("\nCluster summary saved to 'cluster_summary_gicumbi.csv'.")
