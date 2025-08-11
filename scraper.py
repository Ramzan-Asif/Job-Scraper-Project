import requests
import pandas as pd

# Fetch data from RemoteOK API
url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
jobs = res.json()[1:]  # Skip metadata

# Extract job data
data = []
for job in jobs:
    data.append({
        "Title": job.get("position"),
        "Company": job.get("company"),
        "Location": job.get("location"),
        "Tags": ", ".join(job.get("tags", [])),
        "Date": job.get("date"),
        "Description": job.get("description")
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("remoteok_jobs.csv", index=False)
print(f"Saved {len(df)} jobs to remoteok_jobs.csv")
