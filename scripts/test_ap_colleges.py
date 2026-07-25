import pandas as pd
import urllib.request
import urllib.parse
import json
import re

df = pd.read_csv('data/nmc_mbbs_colleges.csv')
ap_pvt = df[(df['State'] == 'Andhra Pradesh') & (df['Management'].isin(['Trust', 'Society', 'Private']))]

print(f"Testing {len(ap_pvt)} AP Private Colleges:")

def search_ddg_snippets(query):
    url = f'https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract snippets and links
            results = []
            links = re.findall(r'<a class="result__url" href="([^"]+)".*?>(.*?)</a>', html)
            snippets = re.findall(r'<a class="result__snippet[^"]*"[^>]*>(.*?)</a>', html)
            for i in range(min(len(links), len(snippets))):
                clean_snippet = re.sub(r'<[^>]+>', '', snippets[i])
                clean_link = links[i][0].strip()
                if 'duckduckgo.com' in clean_link and 'uddg=' in clean_link:
                    match = re.search(r'uddg=([^&]+)', clean_link)
                    if match:
                        clean_link = urllib.parse.unquote(match.group(1))
                results.append((clean_link, clean_snippet))
            return results
    except Exception as e:
        print(f"Search error for {query}: {e}")
        return []

for idx, row in ap_pvt.iterrows():
    name = row['CollegeName']
    slno = row['SlNo']
    print(f"\n--- [{slno}] {name} ---")
    res = search_ddg_snippets(f'"{name}" chairman founder trust political')
    if not res:
        res = search_ddg_snippets(f'{name} founder chairman owner trust')
    for link, snip in res[:3]:
        print(f" Link: {link}\n Snip: {snip[:150]}...")
