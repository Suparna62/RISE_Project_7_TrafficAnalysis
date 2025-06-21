import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('traffic_data.csv')
df['Hour'] = pd.to_datetime(df['TimeSlot'], format='%H:%M').dt.hour

# Line plot - traffic over time
plt.figure(figsize=(10,5))
plt.plot(df['Hour'], df['VehicleCount'], marker='o', color='green')
plt.title('Vehicle Traffic by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Vehicle Count')
plt.grid(True)
plt.xticks(range(0, 24))
plt.tight_layout()
plt.savefig('traffic_line.png')
plt.show()

# Heatmap - simulate hourly trend per location (only one location in this case)
heatmap_df = df.pivot_table(values='VehicleCount', index='Location', columns='Hour')
plt.figure(figsize=(10,2))
sns.heatmap(heatmap_df, cmap='YlOrRd', annot=True, fmt=".0f")
plt.title('Traffic Density Heatmap')
plt.tight_layout()
plt.savefig('traffic_heatmap.png')
plt.show()
