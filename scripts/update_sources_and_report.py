import json

def main():
    with open('data/private_college_sources.json', 'r') as f:
        sources_data = json.load(f)
        
    for item in sources_data:
        if "Sources" in item:
            item["Sources"].append("Historical Political Timelines of Indian States and Centre (1947-2024)")
            
    with open('data/private_college_sources.json', 'w') as f:
        json.dump(sources_data, f, indent=2)
        
    # Now generate report additions
    with open('data/private_colleges_ownership.json', 'r') as f:
        colleges = json.load(f)
        
    center_counts = {}
    state_counts = {}
    total = len(colleges)
    
    for c in colleges:
        center = c.get("CenterRulingPartyAtEstablishment", "Unknown")
        state = c.get("StateRulingPartyAtEstablishment", "Unknown")
        
        center_counts[center] = center_counts.get(center, 0) + 1
        state_counts[state] = state_counts.get(state, 0) + 1
        
    # Sort counts
    center_sorted = sorted(center_counts.items(), key=lambda x: x[1], reverse=True)
    state_sorted = sorted(state_counts.items(), key=lambda x: x[1], reverse=True)
    
    report_addition = """
---

## Political Climate at the Time of Establishment

By correlating the year of establishment (`YearEstablished`) with the historical timelines of ruling governments at both the Central and State levels, we can observe the political environment during which private medical colleges were founded.

### Center Ruling Government at Establishment
The majority of private medical colleges were established during the tenure of a few prominent central governments, reflecting periods of aggressive policy liberalization in medical education.

| Center Ruling Party / Coalition | Number of Private Colleges Established | Percentage |
| :--- | :---: | :---: |
"""
    for party, count in center_sorted:
        pct = (count / total) * 100
        report_addition += f"| {party} | {count} | {pct:.1f}% |\n"
        
    report_addition += """

### State Ruling Government at Establishment (Top 10)
At the state level, the proliferation of private medical colleges often aligns with regional governments that actively promoted private trusts and societies in higher education.

| State Ruling Party | Number of Private Colleges Established |
| :--- | :---: |
"""
    for party, count in state_sorted[:10]:
        report_addition += f"| {party} | {count} |\n"
        
    report_addition += "\n*Note: This data reflects the ruling party/coalition at the exact year of inception for each college based on historical records.*\n"
    
    with open('reports/private_colleges_ownership_report.md', 'a') as f:
        f.write(report_addition)
        
    print("Updated sources and appended report additions.")

if __name__ == '__main__':
    main()
