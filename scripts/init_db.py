import json, pandas as pd

df = pd.read_csv('data/nmc_mbbs_colleges.csv')
pvt = df[df['Management'].isin(['Trust', 'Society', 'Private'])]
print(f"Total target private colleges: {len(pvt)}")

# Create empty structure or load existing
try:
    with open('data/private_colleges_ownership.json', 'r') as f:
        ownership_db = json.load(f)
except Exception:
    ownership_db = []

try:
    with open('data/private_college_sources.json', 'r') as f:
        sources_db = json.load(f)
except Exception:
    sources_db = []

existing_slnos = set(x['SlNo'] for x in ownership_db)
print(f"Already processed: {len(existing_slnos)} / {len(pvt)}")
