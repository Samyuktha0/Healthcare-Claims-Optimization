import pandas as pd

df = pd.read_csv("claims.csv")
anomalies = df[df['amount'] > 10000]
print(f"Flagged {len(anomalies)} anomalies")
