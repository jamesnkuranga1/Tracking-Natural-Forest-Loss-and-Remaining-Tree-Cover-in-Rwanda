# Phase 5: Evaluation – Cluster Quality Assessment

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load clustered data
df = pd.read_csv("gicumbi_clustered.csv")

# 2. Prepare features for evaluation
X = df[['Forest_Area_ha']] if 'Forest_Area_ha' in df.columns else df[['wri_tropical_tree_cover_extent__ha']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Silhouette Score (global cluster quality)
sil_score = silhouette_score(X_scaled, df['Cluster'])
print(f"Silhouette Score: {sil_score:.4f} (closer to 1 means better clustering)")

# 4. Silhouette Samples (individual point quality)
sample_silhouette = silhouette_samples(X_scaled, df['Cluster'])
df['Silhouette_Coefficient'] = sample_silhouette

# 5. Summary by Cluster
summary = df.groupby('Cluster')['Silhouette_Coefficient'].agg(['mean', 'min', 'max', 'std'])
print("\nSilhouette Coefficient Summary per Cluster:")
print(summary)

# 6. Plot: Silhouette Coefficient by Cluster
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Cluster', y='Silhouette_Coefficient', palette='coolwarm')
plt.title("Silhouette Coefficient Distribution per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Silhouette Coefficient")
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Save evaluation results
df.to_csv("gicumbi_evaluation_results.csv", index=False)
print("\nEvaluation results saved to 'gicumbi_evaluation_results.csv'.")
