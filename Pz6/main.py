import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

laptop_df = pd.read_csv("laptop.csv")
microwave_df = pd.read_csv("microwave.csv")
television_df = pd.read_csv("television.csv")

print("Статистика для ноутбука:")
print(laptop_df['Absolute field (µT)'].describe())
print("\nСтатистика для мікрохвильової печі:")
print(microwave_df['Absolute field (µT)'].describe())
print("\nСтатистика для телевізора:")
print(television_df['Absolute field (µT)'].describe())

def detect_anomalies_isolation_forest(df, contamination=0.05):
    X = df[['Absolute field (µT)']].values
    isolation_forest = IsolationForest(contamination=contamination, random_state=42)
    anomalies = isolation_forest.fit_predict(X)
    df['Anomaly'] = anomalies
    return df

def detect_anomalies_lof(df, contamination=0.05, n_neighbors=20):
    X = df[['Absolute field (µT)']].values
    lof = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination)
    anomalies = lof.fit_predict(X)
    df['Anomaly'] = anomalies
    return df

laptop_df_isolation = detect_anomalies_isolation_forest(laptop_df)
laptop_df_lof = detect_anomalies_lof(laptop_df)

microwave_df_isolation = detect_anomalies_isolation_forest(microwave_df)
microwave_df_lof = detect_anomalies_lof(microwave_df)

television_df_isolation = detect_anomalies_isolation_forest(television_df)
television_df_lof = detect_anomalies_lof(television_df)

plt.figure(figsize=(10, 6))
plt.plot(laptop_df['Time (s)'], laptop_df['Absolute field (µT)'], label='Магнітне поле', color='blue')
plt.scatter(laptop_df['Time (s)'][laptop_df['Anomaly'] == -1], laptop_df['Absolute field (µT)'][laptop_df['Anomaly'] == -1], color='red', label='Аномалії (IF)')
plt.xlabel('Час (с)')
plt.ylabel('Абсолютне магнітне поле (µT)')
plt.title('Ноутбук - Виявлення аномалій (Isolation Forest)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(laptop_df['Time (s)'], laptop_df['Absolute field (µT)'], label='Магнітне поле', color='blue')
plt.scatter(laptop_df['Time (s)'][laptop_df['Anomaly'] == -1], laptop_df['Absolute field (µT)'][laptop_df['Anomaly'] == -1], color='green', label='Аномалії (LOF)')
plt.xlabel('Час (с)')
plt.ylabel('Абсолютне магнітне поле (µT)')
plt.title('Ноутбук - Виявлення аномалій (LOF)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(microwave_df['Time (s)'], microwave_df['Absolute field (µT)'], label='Магнітне поле', color='blue')
plt.scatter(microwave_df['Time (s)'][microwave_df['Anomaly'] == -1], microwave_df['Absolute field (µT)'][microwave_df['Anomaly'] == -1], color='red', label='Аномалії (IF)')
plt.xlabel('Час (с)')
plt.ylabel('Абсолютне магнітне поле (µT)')
plt.title('Мікрохвильова піч - Виявлення аномалій (Isolation Forest)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(microwave_df['Time (s)'], microwave_df['Absolute field (µT)'], label='Магнітне поле', color='blue')
plt.scatter(microwave_df['Time (s)'][microwave_df['Anomaly'] == -1], microwave_df['Absolute field (µT)'][microwave_df['Anomaly'] == -1], color='green', label='Аномалії (LOF)')
plt.xlabel('Час (с)')
plt.ylabel('Абсолютне магнітне поле (µT)')
plt.title('Мікрохвильова піч - Виявлення аномалій (LOF)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(television_df['Time (s)'], television_df['Absolute field (µT)'], label='Магнітне поле', color='blue')
plt.scatter(television_df['Time (s)'][television_df['Anomaly'] == -1], television_df['Absolute field (µT)'][television_df['Anomaly'] == -1], color='red', label='Аномалії (IF)')
plt.xlabel('Час (с)')
plt.ylabel('Абсолютне магнітне поле (µT)')
plt.title('Телевізор - Виявлення аномалій (Isolation Forest)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(television_df['Time (s)'], television_df['Absolute field (µT)'], label='Магнітне поле', color='blue')
plt.scatter(television_df['Time (s)'][television_df['Anomaly'] == -1], television_df['Absolute field (µT)'][television_df['Anomaly'] == -1], color='green', label='Аномалії (LOF)')
plt.xlabel('Час (с)')
plt.ylabel('Абсолютне магнітне поле (µT)')
plt.title('Телевізор - Виявлення аномалій (LOF)')
plt.legend()
plt.grid(True)
plt.show()
